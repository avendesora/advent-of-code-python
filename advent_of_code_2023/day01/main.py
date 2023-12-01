from __future__ import annotations

from helpers import read_input_as_string_array
from helpers.logger import get_logger

LOGGER = get_logger("2023-day-01")


DIGITS = {
    "one": "o1e",
    "two": "t2",
    "three": "t3e",
    "four": "4",
    "five": "5e",
    "six": "6",
    "seven": "7",
    "eight": "e8t",
    "nine": "9e",
}


def get_next_number(input_string: str) -> str:
    return next((character for character in input_string if character.isdigit()), "")


def get_number(input_string: str) -> int:
    first_number = get_next_number(input_string)
    last_number = get_next_number(input_string[::-1])
    return int(f"{first_number}{last_number}")


def get_numbers(input_strings: list[str]) -> list[int]:
    return [get_number(input_string) for input_string in input_strings]


def clean_string(input_string: str) -> str:
    cleaned_string = input_string

    for key, value in DIGITS.items():
        cleaned_string = cleaned_string.replace(key, value)

    return cleaned_string


def get_numbers_2(input_strings: list[str]) -> list[int]:
    return [get_number(clean_string(input_string)) for input_string in input_strings]


def part_one(input_strings: list[str]) -> int:
    return sum(get_numbers(input_strings))


def part_two(input_strings: list[str]) -> int:
    return sum(get_numbers_2(input_strings))


if __name__ == "__main__":
    input_data = read_input_as_string_array("input.txt")
    part_one_result = part_one(input_data)
    LOGGER.info("part one = %d", part_one_result)

    input_data2 = read_input_as_string_array("input2.txt")
    part_two_result = part_two(input_data2)
    LOGGER.info("part two = %d", part_two_result)
