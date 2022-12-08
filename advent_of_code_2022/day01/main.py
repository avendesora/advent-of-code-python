from pathlib import Path

from helpers import clean_line


def read_input(filename: Path | str) -> list[list[int]]:
    elves: list[list[int]] = []
    current_food_list: list[int] = []

    with open(filename, encoding="utf-8") as lines:
        for line in lines:
            line = clean_line(line)

            if not line:
                elves.append(current_food_list)
                current_food_list = []
                continue

            current_food_list.append(int(line))

    if current_food_list:
        elves.append(current_food_list)

    return elves


def part_one(elves: list[list[int]]) -> int:
    elves_total_calories: list[int] = _get_elves_total_calories(elves)

    return max(elves_total_calories)


def part_two(elves: list[list[int]]) -> int:
    elves_total_calories: list[int] = _get_elves_total_calories(elves)
    elves_total_calories.sort(reverse=True)

    return sum(elves_total_calories[:3])


def _get_elves_total_calories(elves: list[list[int]]) -> list[int]:
    return [sum(elf) for elf in elves]


if __name__ == "__main__":
    elves_input: list[list[int]] = read_input("input.txt")
    top_elf_total_calories = part_one(elves_input)
    print(top_elf_total_calories)

    top_three_elves_total_calories = part_two(elves_input)
    print(top_three_elves_total_calories)
