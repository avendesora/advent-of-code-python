import os
from pathlib import Path

import pytest

from advent_of_code_2022.day10.main import part_one
from advent_of_code_2022.day10.main import part_two
from advent_of_code_2022.day10.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


@pytest.mark.xfail()
def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data is not None


@pytest.mark.xfail()
def test_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_one(input_data) is not None


@pytest.mark.xfail()
def test_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_two(input_data) is not None
