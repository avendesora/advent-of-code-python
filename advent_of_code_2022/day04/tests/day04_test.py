from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2022.day04.main import part_one
from advent_of_code_2022.day04.main import part_two
from advent_of_code_2022.day04.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == [
        ({2, 3, 4}, {8, 6, 7}),
        ({2, 3}, {4, 5}),
        ({5, 6, 7}, {8, 9, 7}),
        ({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}),
        ({6}, {4, 5, 6}),
        ({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}),
    ]


def test_day_04_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_one(input_data) == 2


def test_day_04_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_two(input_data) == 4
