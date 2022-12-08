import os
from pathlib import Path

from advent_of_code_2022.day02.main import part_one
from advent_of_code_2022.day02.main import part_two
from advent_of_code_2022.day02.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == [
        ["A", "Y"],
        ["B", "X"],
        ["C", "Z"],
    ]


def test_day_02_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_one(input_data) == 15


def test_day_02_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_two(input_data) == 12
