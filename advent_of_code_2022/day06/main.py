from __future__ import annotations

from pathlib import Path

from helpers import read_input_as_string_array


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
    print(part_one(day6_input))
    print(part_two(day6_input))
