from pathlib import Path

from helpers import read_input_as_string_array


def read_input(filename: Path | str) -> list[tuple[set[int], set[int]]]:
    pairs = []

    for line in read_input_as_string_array(filename):
        pair1, pair2 = line.split(",")
        pairs.append((get_range(pair1), get_range(pair2)))

    return pairs


def get_range(pair: str) -> set[int]:
    pair_min, pair_max = pair.split("-")
    return set(range(int(pair_min), int(pair_max) + 1))


def does_fully_contain(range1: set[int], range2: set[int]) -> bool:
    return range1.issubset(range2) or range2.issubset(range1)


def does_overlap(range1: set[int], range2: set[int]) -> bool:
    return len(range1.intersection(range2)) > 0


def part_one(input_data: list[tuple[set[int], set[int]]]) -> int:
    return sum(
        bool(does_fully_contain(range1, range2)) for range1, range2 in input_data
    )


def part_two(input_data: list[tuple[set[int], set[int]]]) -> int:
    return sum(bool(does_overlap(range1, range2)) for range1, range2 in input_data)


if __name__ == "__main__":
    day4_input = read_input("input.txt")
    print(part_one(day4_input))
    print(part_two(day4_input))
