from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2023.day01.main import part_one
from advent_of_code_2023.day01.main import part_two
from helpers import read_input_as_string_array

CURRENT_DIRECTORY = Path(Path(os.path.realpath(__file__)).parent)


def test_part_one() -> None:
    part_one_input = read_input_as_string_array(CURRENT_DIRECTORY / "sample_input.txt")
    result = part_one(part_one_input)

    assert result == 142


def test_part_two() -> None:
    part_two_input = read_input_as_string_array(
        CURRENT_DIRECTORY / "sample_input_2.txt",
    )
    result = part_two(part_two_input)

    assert result == 281
