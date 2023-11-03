from __future__ import annotations

import os
from pathlib import Path

import pytest

from advent_of_code_2021.day17.main import part_one
from advent_of_code_2021.day17.main import part_two
from advent_of_code_2021.day17.main import read_input

CURRENT_DIRECTORY = Path(Path(os.path.realpath(__file__)).parent)


@pytest.mark.xfail()
def test_read_input() -> None:
    x_values, y_values = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert x_values == (20, 30)
    assert y_values == (-10, -5)


@pytest.mark.xfail()
def test_day_01_part_one() -> None:
    x_values, y_values = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    velocity = part_one(x_values[0], x_values[1], y_values[0], y_values[1])
    assert velocity == (6, 9)


@pytest.mark.xfail()
def test_day_01_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_two(input_data) is not None
