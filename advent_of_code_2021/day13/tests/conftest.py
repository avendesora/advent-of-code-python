from __future__ import annotations

import pytest

from advent_of_code_2021.day13.main import Axis
from helpers import Point2D


@pytest.fixture()
def sample_data() -> tuple[list[Point2D], list[tuple[Axis, int]]]:
    return (
        [
            Point2D(6, 10),
            Point2D(0, 14),
            Point2D(9, 10),
            Point2D(0, 3),
            Point2D(10, 4),
            Point2D(4, 11),
            Point2D(6, 0),
            Point2D(6, 12),
            Point2D(4, 1),
            Point2D(0, 13),
            Point2D(10, 12),
            Point2D(3, 4),
            Point2D(3, 0),
            Point2D(8, 4),
            Point2D(1, 10),
            Point2D(2, 14),
            Point2D(8, 10),
            Point2D(9, 0),
        ],
        [
            (Axis.Y, 7),
            (Axis.X, 5),
        ],
    )


@pytest.fixture()
def initial_pattern() -> list[list[bool]]:
    return [
        [False, False, False, True, False, False, True, False, False, True, False],
        [False, False, False, False, True, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False],
        [True, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, True, False, False, False, False, True, False, True],
        [False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False],
        [False, True, False, False, False, False, True, False, True, True, False],
        [False, False, False, False, True, False, False, False, False, False, False],
        [False, False, False, False, False, False, True, False, False, False, True],
        [True, False, False, False, False, False, False, False, False, False, False],
        [True, False, True, False, False, False, False, False, False, False, False],
    ]


@pytest.fixture()
def pattern_string() -> str:
    return """...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
"""


@pytest.fixture()
def folded_pattern_y() -> list[list[bool]]:
    return [
        [True, False, True, True, False, False, True, False, False, True, False],
        [True, False, False, False, True, False, False, False, False, False, False],
        [False, False, False, False, False, False, True, False, False, False, True],
        [True, False, False, False, True, False, False, False, False, False, False],
        [False, True, False, True, False, False, True, False, True, True, True],
        [False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False],
    ]


@pytest.fixture()
def folded_pattern_y_string() -> str:
    return """#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
"""


@pytest.fixture()
def folded_pattern_x() -> list[list[bool]]:
    return [
        [True, True, True, True, True],
        [True, False, False, False, True],
        [True, False, False, False, True],
        [True, False, False, False, True],
        [True, True, True, True, True],
        [False, False, False, False, False],
        [False, False, False, False, False],
    ]


@pytest.fixture()
def folded_pattern_x_string() -> str:
    return """#####
#...#
#...#
#...#
#####
.....
.....
"""
