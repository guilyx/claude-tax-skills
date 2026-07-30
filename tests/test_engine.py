"""Tests for the shared computation pipeline.

The fixture below is a deliberately artificial country so the expected numbers
can be worked out by hand in the test itself. Anything that depends on a real
country's rates belongs in test_countries.py, which asserts properties rather
than exact figures.
"""

import pytest

from taxcalc.engine import Profile, compute

COUNTRY = {
    "country": "Testland",
    "iso2": "TL",
    "tax_year": 2025,
    "currency": "TLD",
    "income_tax": {
        "type": "progressive",
        "brackets": [
            {"up_to": 10_000, "rate": 0.0},
            {"up_to": 50_000, "rate": 0.20},
            {"up_to": None, "rate": 0.40},
        ],
    },
    "standard_deduction": {"name": "Standard deduction", "amount": 5_000},
    "social_security": {
        "employee": [
            {"name": "Pension", "rate": 0.10, "ceiling": 60_000, "deductible": True},
            {"name": "Health", "rate": 0.02, "deductible": False},
        ],
        "employer": [{"name": "Pension", "rate": 0.10, "ceiling": 60_000}],
    },
    "reporting": {
        "tax_year_end": "31 December",
        "authority": "Testland Revenue",
        "deadlines": [{"date": "x", "what": "y"}],
    },
    "sources": [{"name": "n/a", "url": "https://example.invalid"}],
}


def test_deductible_contributions_reduce_taxable_income_but_others_do_not():
    result = compute(COUNTRY, Profile(employment_income=100_000))
    # Pension is capped at 60,000 of base -> 6,000, and is deductible.
    # Health is 2% of 100,000 -> 2,000, and is not.
    assert result.employee_social_security == pytest.approx(8_000)
    assert result.taxable_income == pytest.approx(100_000 - 6_000 - 5_000)


def test_net_income_reconciles_with_its_components():
    result = compute(COUNTRY, Profile(employment_income=80_000))
    assert result.net_income == pytest.approx(
        result.gross_income - result.employee_social_security - result.total_income_tax
    )


def test_employer_contributions_do_not_touch_the_employee_result():
    result = compute(COUNTRY, Profile(employment_income=50_000))
    assert result.employer_social_security > 0
    assert result.net_income == pytest.approx(
        50_000 - result.employee_social_security - result.total_income_tax
    )


def test_marginal_wedge_reflects_the_contribution_ceiling():
    """Above the pension ceiling the wedge falls, even with the rate unchanged.

    This is the behaviour that surprises people on payslips, and it is the main
    reason the engine measures the wedge numerically instead of reading a rate
    off the bracket table. A flat income tax is used here so that the ceiling is
    the only thing that can move the answer.
    """
    country = {**COUNTRY, "income_tax": {"type": "flat", "rate": 0.30}}
    below = compute(country, Profile(employment_income=55_000))
    above = compute(country, Profile(employment_income=70_000))
    assert above.marginal_wedge < below.marginal_wedge
    # Below the ceiling: 10% pension (deductible) + 2% health + 30% of the
    # remaining 90 = 39%. Above it, only health and the full 30% remain.
    assert below.marginal_wedge == pytest.approx(0.39)
    assert above.marginal_wedge == pytest.approx(0.32)


def test_income_splitting_lowers_tax_for_a_couple():
    country = {
        **COUNTRY,
        "income_tax": {
            **COUNTRY["income_tax"],
            "by_filing_status": {
                "single": {"income_splitting_factor": 1},
                "married_joint": {"income_splitting_factor": 2},
            },
        },
    }
    single = compute(country, Profile(employment_income=100_000, filing_status="single"))
    couple = compute(country, Profile(employment_income=100_000, filing_status="married_joint"))
    assert couple.total_income_tax < single.total_income_tax


def test_non_refundable_credits_cannot_go_below_zero_tax():
    country = {
        **COUNTRY,
        "credits": [{"name": "Huge credit", "amount": 999_999, "refundable": False}],
    }
    result = compute(country, Profile(employment_income=40_000))
    assert result.total_income_tax == pytest.approx(0.0)


def test_refundable_credits_may_produce_a_negative_liability():
    country = {
        **COUNTRY,
        "credits": [{"name": "Refundable benefit", "amount": 20_000, "refundable": True}],
    }
    result = compute(country, Profile(employment_income=40_000))
    assert result.total_income_tax < 0


def test_tapered_allowance_creates_a_higher_marginal_rate_in_the_taper_zone():
    country = {
        **COUNTRY,
        "personal_allowance": {
            "name": "Tapered allowance",
            "amount": 12_000,
            "taper": {"threshold": 60_000, "rate": 0.5, "floor": 0},
        },
    }
    inside = compute(country, Profile(employment_income=70_000))
    outside = compute(country, Profile(employment_income=120_000))
    assert inside.marginal_wedge > outside.marginal_wedge


def test_zero_income_is_handled_without_dividing_by_zero():
    result = compute(COUNTRY, Profile(employment_income=0))
    assert result.total_income_tax == 0
    assert result.effective_tax_rate == 0
    assert result.net_income == 0


def test_surcharge_on_tax_compounds_on_top_of_the_schedule():
    country = {**COUNTRY, "surcharges": [{"name": "Levy", "base": "tax", "rate": 0.10}]}
    plain = compute(COUNTRY, Profile(employment_income=60_000))
    surcharged = compute(country, Profile(employment_income=60_000))
    assert surcharged.total_income_tax == pytest.approx(plain.total_income_tax * 1.10)
