import os
from pathlib import Path

from advent_of_code_2022.day01.main import part_one
from advent_of_code_2022.day01.main import part_two
from advent_of_code_2022.day01.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input() -> None:
    elves_input = read_input(CURRENT_DIRECTORY / "sample_input.txt")

    expected_result = [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]

    assert elves_input == expected_result


def test_day_01_part_one() -> None:
    elves_input = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    max_calories = part_one(elves_input)

    assert max_calories == 24000


def test_day_01_part_two() -> None:
    elves_input = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    max_calories = part_two(elves_input)

    assert max_calories == 45000
