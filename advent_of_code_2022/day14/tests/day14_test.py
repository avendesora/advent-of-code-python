from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2022.day14.main import part_one
from advent_of_code_2022.day14.main import part_two
from advent_of_code_2022.day14.main import read_input
from helpers import Point2D

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == [
        [
            Point2D(x=498, y=4),
            Point2D(x=498, y=6),
            Point2D(x=496, y=6),
        ],
        [
            Point2D(x=503, y=4),
            Point2D(x=502, y=4),
            Point2D(x=502, y=9),
            Point2D(x=494, y=9),
        ],
    ]


def test_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_one(input_data) == 24


def test_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_two(input_data) == 93
