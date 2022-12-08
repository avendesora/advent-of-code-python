import string
from pathlib import Path

from helpers import read_input_as_string_array


def read_input(filename: Path | str) -> list[str]:
    return read_input_as_string_array(filename)


def get_priority(character: str) -> int:
    return string.ascii_letters.index(character) + 1


def part_one(input_data: list[str]) -> int:
    priority_sum = 0

    for rucksack in input_data:
        half_length = len(rucksack) // 2
        compartment1 = rucksack[:half_length]
        compartment2 = rucksack[half_length:]
        shared_item = set(compartment1).intersection(set(compartment2)).pop()
        priority_sum += get_priority(shared_item)

    return priority_sum


def part_two(input_data: list[str]) -> int:
    priority_sum = 0

    for index, rucksack in enumerate(input_data[2::3]):
        real_index = (index + 1) * 3 - 1
        badge = (
            set(rucksack)
            .intersection(set(input_data[real_index - 1]))
            .intersection(set(input_data[real_index - 2]))
            .pop()
        )
        priority_sum += get_priority(badge)

    return priority_sum


if __name__ == "__main__":
    day3_input = read_input("input.txt")
    print(part_one(day3_input))
    print(part_two(day3_input))
