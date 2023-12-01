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


def get_next_number(line: str) -> str:
    return next((character for character in line if character.isdigit()), "")


def get_number(line: str) -> int:
    return int(f"{get_next_number(line)}{get_next_number(line[::-1])}")


def clean_line(line: str) -> str:
    cleaned_line = line

    for key, value in DIGITS.items():
        cleaned_line = cleaned_line.replace(key, value)

    return cleaned_line


def part_one(input_data: list[str]) -> int:
    return sum(get_number(line) for line in input_data)


def part_two(input_data: list[str]) -> int:
    return sum(get_number(clean_line(line)) for line in input_data)


if __name__ == "__main__":
    input_data1 = read_input_as_string_array("input.txt")
    part_one_result = part_one(input_data1)
    LOGGER.info("part one = %d", part_one_result)

    input_data2 = read_input_as_string_array("input2.txt")
    part_two_result = part_two(input_data2)
    LOGGER.info("part two = %d", part_two_result)
