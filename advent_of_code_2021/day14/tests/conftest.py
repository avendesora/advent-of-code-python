from __future__ import annotations

import pytest


@pytest.fixture()
def sample_data() -> tuple[str, dict[str, str]]:
    return (
        "NNCB",
        {
            "BB": "N",
            "BC": "B",
            "BH": "H",
            "BN": "B",
            "CB": "H",
            "CC": "N",
            "CH": "B",
            "CN": "C",
            "HB": "C",
            "HC": "B",
            "HH": "N",
            "HN": "C",
            "NB": "B",
            "NC": "B",
            "NH": "C",
            "NN": "C",
        },
    )


@pytest.fixture()
def pairs() -> dict[str, int]:
    return {
        "CB": 1,
        "NC": 1,
        "NN": 1,
    }
