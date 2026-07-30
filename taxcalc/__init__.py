"""taxcalc - a small, auditable personal income tax engine.

The package deliberately contains no country-specific logic. Every country is
described by a JSON file in ``data/countries/``; this package only knows how to
apply the handful of *shapes* that tax systems come in (progressive brackets,
flat rates, piecewise polynomial formulas, capped social contributions,
surcharges and credits).

That split matters: when a rate changes, you edit one number in JSON instead of
hunting through code, and the arithmetic stays identical across all 30
countries so results are comparable.
"""

from .engine import ComputationResult, compute
from .loader import (
    CountryNotFound,
    available_countries,
    load_country,
)

__version__ = "0.1.0"
__all__ = [
    "ComputationResult",
    "CountryNotFound",
    "available_countries",
    "compute",
    "load_country",
]
