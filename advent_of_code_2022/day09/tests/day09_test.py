import os
from pathlib import Path

from advent_of_code_2022.day09.main import Direction
from advent_of_code_2022.day09.main import Motion
from advent_of_code_2022.day09.main import part_one
from advent_of_code_2022.day09.main import part_two
from advent_of_code_2022.day09.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == [
        Motion(direction=Direction.RIGHT, number_of_steps=4),
        Motion(direction=Direction.UP, number_of_steps=4),
        Motion(direction=Direction.LEFT, number_of_steps=3),
        Motion(direction=Direction.DOWN, number_of_steps=1),
        Motion(direction=Direction.RIGHT, number_of_steps=4),
        Motion(direction=Direction.DOWN, number_of_steps=1),
        Motion(direction=Direction.LEFT, number_of_steps=5),
        Motion(direction=Direction.RIGHT, number_of_steps=2),
    ]


def test_day_09_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_one(input_data) == 13


def test_read_input2() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input2.txt")
    assert input_data == [
        Motion(direction=Direction.RIGHT, number_of_steps=5),
        Motion(direction=Direction.UP, number_of_steps=8),
        Motion(direction=Direction.LEFT, number_of_steps=8),
        Motion(direction=Direction.DOWN, number_of_steps=3),
        Motion(direction=Direction.RIGHT, number_of_steps=17),
        Motion(direction=Direction.DOWN, number_of_steps=10),
        Motion(direction=Direction.LEFT, number_of_steps=25),
        Motion(direction=Direction.UP, number_of_steps=20),
    ]


def test_day_09_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input2.txt")
    assert part_two(input_data) == 36
