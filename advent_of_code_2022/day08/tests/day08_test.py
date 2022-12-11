from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2022.day08.main import part_one
from advent_of_code_2022.day08.main import part_two
from advent_of_code_2022.day08.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]


def test_day_08_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_one(input_data) == 21


def test_day_08_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_two(input_data) == 8
