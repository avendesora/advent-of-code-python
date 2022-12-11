from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2021.day09.main import get_basins
from advent_of_code_2021.day09.main import get_product_size
from advent_of_code_2021.day09.main import get_risk_level
from helpers import read_input_as_2d_int_array

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_day_09_read_input() -> None:
    sample_input = read_input_as_2d_int_array(CURRENT_DIRECTORY / "sample_input.txt")
    assert sample_input == [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]


def test_day_09_part_one() -> None:
    sample_input = read_input_as_2d_int_array(CURRENT_DIRECTORY / "sample_input.txt")
    assert get_risk_level(sample_input) == 15


def test_day_09_part_two() -> None:
    sample_input = read_input_as_2d_int_array(CURRENT_DIRECTORY / "sample_input.txt")
    basins: list[set[str]] = get_basins(sample_input)
    assert get_product_size(basins, 3) == 1134
