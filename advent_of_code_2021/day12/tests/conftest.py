from __future__ import annotations

import pytest


@pytest.fixture()
def sample_data1() -> list[tuple[str, ...]]:
    return [
        ("start", "A"),
        ("start", "b"),
        ("A", "c"),
        ("A", "b"),
        ("b", "d"),
        ("A", "end"),
        ("b", "end"),
    ]


@pytest.fixture()
def sample_data2() -> list[tuple[str, ...]]:
    return [
        ("dc", "end"),
        ("HN", "start"),
        ("start", "kj"),
        ("dc", "start"),
        ("dc", "HN"),
        ("LN", "dc"),
        ("HN", "end"),
        ("kj", "sa"),
        ("kj", "HN"),
        ("kj", "dc"),
    ]


@pytest.fixture()
def sample_data3() -> list[tuple[str, ...]]:
    return [
        ("fs", "end"),
        ("he", "DX"),
        ("fs", "he"),
        ("start", "DX"),
        ("pj", "DX"),
        ("end", "zg"),
        ("zg", "sl"),
        ("zg", "pj"),
        ("pj", "he"),
        ("RW", "he"),
        ("fs", "DX"),
        ("pj", "RW"),
        ("zg", "RW"),
        ("start", "pj"),
        ("he", "WI"),
        ("zg", "he"),
        ("pj", "fs"),
        ("start", "RW"),
    ]


@pytest.fixture()
def valid_paths1() -> set[str]:
    return {
        "start, A, b, A, c, A, end",
        "start, A, b, A, end",
        "start, A, b, end",
        "start, A, c, A, b, A, end",
        "start, A, c, A, b, end",
        "start, A, c, A, end",
        "start, A, end",
        "start, b, A, c, A, end",
        "start, b, A, end",
        "start, b, end",
    }


@pytest.fixture()
def valid_paths2() -> set[str]:
    return {
        "start, HN, dc, HN, end",
        "start, HN, dc, HN, kj, HN, end",
        "start, HN, dc, end",
        "start, HN, dc, kj, HN, end",
        "start, HN, end",
        "start, HN, kj, HN, dc, HN, end",
        "start, HN, kj, HN, dc, end",
        "start, HN, kj, HN, end",
        "start, HN, kj, dc, HN, end",
        "start, HN, kj, dc, end",
        "start, dc, HN, end",
        "start, dc, HN, kj, HN, end",
        "start, dc, end",
        "start, dc, kj, HN, end",
        "start, kj, HN, dc, HN, end",
        "start, kj, HN, dc, end",
        "start, kj, HN, end",
        "start, kj, dc, HN, end",
        "start, kj, dc, end",
    }


@pytest.fixture()
def valid_paths1b() -> set[str]:
    return {
        "start, A, b, A, b, A, c, A, end",
        "start, A, b, A, b, A, end",
        "start, A, b, A, b, end",
        "start, A, b, A, c, A, b, A, end",
        "start, A, b, A, c, A, b, end",
        "start, A, b, A, c, A, c, A, end",
        "start, A, b, A, c, A, end",
        "start, A, b, A, end",
        "start, A, b, d, b, A, c, A, end",
        "start, A, b, d, b, A, end",
        "start, A, b, d, b, end",
        "start, A, b, end",
        "start, A, c, A, b, A, b, A, end",
        "start, A, c, A, b, A, b, end",
        "start, A, c, A, b, A, c, A, end",
        "start, A, c, A, b, A, end",
        "start, A, c, A, b, d, b, A, end",
        "start, A, c, A, b, d, b, end",
        "start, A, c, A, b, end",
        "start, A, c, A, c, A, b, A, end",
        "start, A, c, A, c, A, b, end",
        "start, A, c, A, c, A, end",
        "start, A, c, A, end",
        "start, A, end",
        "start, b, A, b, A, c, A, end",
        "start, b, A, b, A, end",
        "start, b, A, b, end",
        "start, b, A, c, A, b, A, end",
        "start, b, A, c, A, b, end",
        "start, b, A, c, A, c, A, end",
        "start, b, A, c, A, end",
        "start, b, A, end",
        "start, b, d, b, A, c, A, end",
        "start, b, d, b, A, end",
        "start, b, d, b, end",
        "start, b, end",
    }
