from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2021.day03.main import get_co2_scrubber_rating
from advent_of_code_2021.day03.main import get_gamma_and_epsilon_rates
from advent_of_code_2021.day03.main import get_life_support_rating
from advent_of_code_2021.day03.main import get_oxygen_generator_rating
from advent_of_code_2021.day03.main import get_power_consumption
from advent_of_code_2021.day03.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == [
        [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    ]


def test_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    gamma_rate, epsilon_rate = get_gamma_and_epsilon_rates(input_data)
    power_consumption = get_power_consumption(gamma_rate, epsilon_rate)
    assert power_consumption == 198


def test_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    oxygen_generator_rating = get_oxygen_generator_rating(input_data)
    co2_scrubber_rating = get_co2_scrubber_rating(input_data)
    life_support_rating = get_life_support_rating(
        oxygen_generator_rating, co2_scrubber_rating
    )
    assert life_support_rating == 230
