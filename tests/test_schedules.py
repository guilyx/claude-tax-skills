"""Tests for the rate-schedule primitives.

These use small invented schedules rather than real countries, so they keep
passing when a rate changes in the data files. Country-specific expectations
live in test_countries.py.
"""

import pytest

from taxcalc.schedules import (
    apply_schedule,
    contribution_amount,
    marginal_rate,
    piecewise_polynomial_tax,
    progressive_tax,
)

BRACKETS = [
    {"up_to": 10_000, "rate": 0.0},
    {"up_to": 30_000, "rate": 0.20},
    {"up_to": None, "rate": 0.40},
]


def test_zero_and_negative_income_produce_no_tax():
    assert progressive_tax(0, BRACKETS) == 0
    assert progressive_tax(-5_000, BRACKETS) == 0


def test_tax_is_charged_only_on_the_slice_inside_each_band():
    assert progressive_tax(10_000, BRACKETS) == 0
    assert progressive_tax(20_000, BRACKETS) == pytest.approx(2_000)
    assert progressive_tax(30_000, BRACKETS) == pytest.approx(4_000)
    assert progressive_tax(50_000, BRACKETS) == pytest.approx(4_000 + 8_000)


def test_marginal_rate_follows_the_band_the_income_lands_in():
    assert marginal_rate(5_000, BRACKETS) == 0.0
    assert marginal_rate(20_000, BRACKETS) == 0.20
    assert marginal_rate(100_000, BRACKETS) == 0.40


def test_a_bracket_boundary_belongs_to_the_lower_band():
    # Published tables say "up to and including", so income exactly at a
    # threshold must not attract the higher rate.
    assert marginal_rate(30_000, BRACKETS) == 0.20


def test_flat_and_none_schedules():
    assert apply_schedule(50_000, {"type": "flat", "rate": 0.22}) == pytest.approx(11_000)
    assert apply_schedule(50_000, {"type": "none"}) == 0


def test_unknown_schedule_type_is_rejected_rather_than_silently_zero():
    with pytest.raises(ValueError):
        apply_schedule(1_000, {"type": "made_up"})


def test_piecewise_polynomial_matches_a_hand_computed_linear_zone():
    zones = [
        {"up_to": 10_000, "coeffs": [], "constant": 0},
        {"up_to": None, "offset": 0, "divisor": 1, "coeffs": [0.4, 0], "constant": -4_000},
    ]
    assert piecewise_polynomial_tax(5_000, zones) == 0
    assert piecewise_polynomial_tax(20_000, zones) == pytest.approx(4_000)


def test_polynomial_needs_its_constant_term():
    # A coefficient list of [0.4] means the constant polynomial 0.4, not 0.4*y.
    # This is exactly the mistake that made the German formula return negative
    # tax, so it is worth pinning down.
    zones = [{"up_to": None, "offset": 0, "divisor": 1, "coeffs": [0.4], "constant": 0}]
    assert piecewise_polynomial_tax(20_000, zones) == pytest.approx(0.4)


class TestContributions:
    def test_ceiling_caps_the_charged_base(self):
        rule = {"rate": 0.10, "ceiling": 50_000}
        assert contribution_amount(40_000, rule) == pytest.approx(4_000)
        assert contribution_amount(90_000, rule) == pytest.approx(5_000)

    def test_floor_can_exempt_or_reduce_the_base(self):
        exempt_below = {"rate": 0.10, "floor": 20_000}
        assert contribution_amount(15_000, exempt_below) == 0
        assert contribution_amount(30_000, exempt_below) == pytest.approx(3_000)

        reduce_base = {"rate": 0.10, "floor": 20_000, "floor_mode": "reduce_base"}
        assert contribution_amount(30_000, reduce_base) == pytest.approx(1_000)

    def test_floor_and_ceiling_combine_to_form_a_band(self):
        rule = {"rate": 0.08, "floor": 12_570, "floor_mode": "reduce_base", "ceiling": 37_700}
        assert contribution_amount(60_000, rule) == pytest.approx(37_700 * 0.08)

    def test_fixed_contributions_are_flat_but_need_some_income(self):
        # Flat contributions do not scale with earnings, but they attach to
        # having earnings: charging them against zero income would make net
        # income negative for someone who earned nothing at all.
        rule = {"type": "fixed", "amount": 1_136}
        assert contribution_amount(1, rule) == 1_136
        assert contribution_amount(500_000, rule) == 1_136
        assert contribution_amount(0, rule) == 0
