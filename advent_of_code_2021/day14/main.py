from __future__ import annotations

from pathlib import Path

from helpers import clean_line


def read_input(filename: Path | str) -> tuple[str, dict[str, str]]:
    polymer_template_input: str
    pair_insertion_rules_input: dict[str, str] = {}
    blank_line_found: bool = False

    with open(filename, encoding="utf-8") as lines:
        for line in lines:
            cleaned_line = clean_line(line).strip()

            if len(cleaned_line) == 0:
                blank_line_found = True
                continue

            if not blank_line_found:
                polymer_template_input = cleaned_line
                continue

            pair_input, character_input = cleaned_line.split(" -> ")
            pair_insertion_rules_input[pair_input] = character_input

    return polymer_template_input, pair_insertion_rules_input


def apply_rules(polymer: str, rules: dict[str, str]) -> str:
    pairs: list[str] = []
    new_polymer_string: str = ""

    for index, character in enumerate(polymer):
        try:
            pairs.append(character + polymer[index + 1])
        except IndexError:
            continue

    for pair in pairs:
        value_to_insert = rules.get(pair, "")

        if len(new_polymer_string) == 0:
            new_polymer_string += pair[0]

        new_polymer_string += value_to_insert + pair[1]

    return new_polymer_string


def get_distinct_characters(polymer: str, rules: dict[str, str]) -> set[str]:
    distinct_characters: set[str] = set(polymer)

    for key, value in rules.items():
        for character in key:
            distinct_characters.add(character)

        for character in value:
            distinct_characters.add(character)

    return distinct_characters


def count_characters(polymer: str, distinct_characters: set[str]) -> dict[str, int]:
    return {character: polymer.count(character) for character in distinct_characters}


def evaluate_counts(
    polymer: str,
    distinct_characters: set[str],
) -> tuple[str, int, str, int]:
    return _evaluate_counts_common(count_characters(polymer, distinct_characters))


def evaluate_counts_part_two(
    pairs: dict[str, int],
    polymer: str,
) -> tuple[str, int, str, int]:
    return _evaluate_counts_common(get_character_counts(pairs, polymer[-1]))


def _evaluate_counts_common(
    character_counts: dict[str, int],
) -> tuple[str, int, str, int]:
    most_common_element: str = ""
    most_common_quantity: int = 0
    least_common_element: str = ""
    least_common_quantity: int = 0

    for character, count in character_counts.items():
        if least_common_quantity == 0 or least_common_quantity > count:
            least_common_element = character
            least_common_quantity = count

        if count > most_common_quantity:
            most_common_element = character
            most_common_quantity = count

    return (
        most_common_element,
        most_common_quantity,
        least_common_element,
        least_common_quantity,
    )


def get_pairs_from_polymer(polymer: str) -> dict[str, int]:
    pairs: dict[str, int] = {}

    for index, character in enumerate(polymer):
        try:
            pair: str = character + polymer[index + 1]
            pair_count: int = pairs.get(pair, 0)
            pairs[pair] = pair_count + 1
        except IndexError:
            continue

    return pairs


def update_pairs(pairs: dict[str, int], rules: dict[str, str]) -> dict[str, int]:
    updated_pairs: dict[str, int] = {}

    for pair, count in pairs.items():
        if pair not in rules:
            pair_count: int = updated_pairs.get(pair, 0)
            pair_count += count
            updated_pairs[pair] = pair_count
            continue

        additional_character: str = rules.get(pair, "")

        new_pair1: str = pair[0] + additional_character
        new_pair2: str = additional_character + pair[1]

        new_pair_count1: int = updated_pairs.get(new_pair1, 0)
        new_pair_count2: int = updated_pairs.get(new_pair2, 0)

        new_pair_count1 += count
        new_pair_count2 += count

        updated_pairs[new_pair1] = new_pair_count1
        updated_pairs[new_pair2] = new_pair_count2

    return updated_pairs


def get_character_counts(pairs: dict[str, int], end_character: str) -> dict[str, int]:
    character_counts: dict[str, int] = {}

    # only count the start characters in the pair, because the end character
    # is the start character for the next pair, except for the final pair
    for pair, count in pairs.items():
        character_counts[pair[0]] = character_counts.get(pair[0], 0) + count

    # count the end character for the final pair
    character_counts[end_character] = character_counts.get(end_character, 0) + 1

    return character_counts


if __name__ == "__main__":
    # Part One
    polymer_template, pair_insertion_rules = read_input("input.txt")
    characters: set[str] = get_distinct_characters(
        polymer_template,
        pair_insertion_rules,
    )

    for _ in range(10):
        polymer_template = apply_rules(polymer_template, pair_insertion_rules)

    largest_element, largest_count, smallest_element, smallest_count = evaluate_counts(
        polymer_template,
        characters,
    )

    print(f"Most common element ({largest_element}, {largest_count}).")
    print(f"Least common element ({smallest_element}, {smallest_count}).")
    print(f"Difference = {largest_count - smallest_count}.")

    # Part Two
    polymer_template, pair_insertion_rules = read_input("input.txt")
    initial_pairs = get_pairs_from_polymer(polymer_template)

    for _ in range(40):
        initial_pairs = update_pairs(initial_pairs, pair_insertion_rules)

    (
        largest_element,
        largest_count,
        smallest_element,
        smallest_count,
    ) = evaluate_counts_part_two(initial_pairs, polymer_template)

    print(f"Most common element ({largest_element}, {largest_count}).")
    print(f"Least common element ({smallest_element}, {smallest_count}).")
    print(f"Difference = {largest_count - smallest_count}.")
