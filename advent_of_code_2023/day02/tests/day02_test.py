from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2023.day02.main import part_one
from advent_of_code_2023.day02.main import part_two
from advent_of_code_2023.day02.main import read_input

CURRENT_DIRECTORY = Path(Path(os.path.realpath(__file__)).parent)


def test_part_one() -> None:
    part_one_input = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    result = part_one(part_one_input)

    assert result == 8


def test_part_two() -> None:
    part_one_input = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    result = part_two(part_one_input)

    assert result == 2286
