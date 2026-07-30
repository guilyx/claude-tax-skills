"""Locate and load country parameter files."""

from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Any


class CountryNotFound(KeyError):
    """Raised when no data file matches the requested country."""


def data_dir() -> Path:
    """Directory holding the country JSON files.

    ``TAXCALC_DATA_DIR`` lets a caller point at a patched copy of the data (for
    example, a fork with employer-specific parameters) without touching the
    package.
    """
    override = os.environ.get("TAXCALC_DATA_DIR")
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parent.parent / "data" / "countries"


@lru_cache(maxsize=1)
def _index() -> dict[str, Path]:
    index: dict[str, Path] = {}
    for path in sorted(data_dir().glob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:  # pragma: no cover - surfaced by validate
            raise ValueError(f"{path.name} is not valid JSON: {exc}") from exc
        for key in (payload.get("iso2", ""), payload.get("country", ""), path.stem):
            if key:
                index[key.lower().replace(" ", "-")] = path
    return index


def available_countries() -> list[dict[str, Any]]:
    """Summary of every country in the dataset, sorted by name."""
    seen: dict[str, dict[str, Any]] = {}
    for path in sorted(data_dir().glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        seen[payload["iso2"]] = {
            "iso2": payload["iso2"],
            "country": payload["country"],
            "currency": payload["currency"],
            "tax_year": payload["tax_year"],
            "skills": payload.get("skills", {}),
        }
    return sorted(seen.values(), key=lambda item: item["country"])


def load_country(key: str) -> dict[str, Any]:
    """Load one country by ISO-3166 alpha-2 code, name, or file stem."""
    normalised = key.lower().replace(" ", "-")
    path = _index().get(normalised)
    if path is None:
        known = ", ".join(sorted({c["iso2"] for c in available_countries()}))
        raise CountryNotFound(f"unknown country {key!r}; available: {known}")
    return json.loads(path.read_text(encoding="utf-8"))
