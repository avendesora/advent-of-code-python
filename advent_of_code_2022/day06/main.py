from __future__ import annotations

from typing import TYPE_CHECKING

from helpers import read_input_as_string_array
from helpers.logger import get_logger

if TYPE_CHECKING:
    from pathlib import Path


LOGGER = get_logger("2022-day-06")


def read_input(filename: Path | str) -> str:
    return read_input_as_string_array(filename)[0]


def find_sequence_index(input_data: str, sequence_length: int) -> int | None:
    if sequence_length > len(input_data):
        return None

    for index in range(sequence_length - 1, len(input_data)):
        sequence = input_data[index - sequence_length + 1 : index + 1]

        if len(set(sequence)) == sequence_length:
            return index + 1

    return None


def part_one(input_data: str) -> int | None:
    return find_sequence_index(input_data, 4)


def part_two(input_data: str) -> int | None:
    return find_sequence_index(input_data, 14)


if __name__ == "__main__":
    day6_input = read_input("input.txt")
    LOGGER.info(part_one(day6_input))
    LOGGER.info(part_two(day6_input))
