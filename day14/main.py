from helpers import clean_line


def read_input(filename: str) -> tuple[str, dict[str, str]]:
    polymer_template_input: str
    pair_insertion_rules_input: dict[str, str] = {}
    blank_line_found: bool = False

    with open(filename, "r", encoding="utf-8") as lines:
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
    distinct_characters: set[str] = set()

    for character in polymer:
        distinct_characters.add(character)

    for key, value in rules.items():
        for character in key:
            distinct_characters.add(character)

        for character in value:
            distinct_characters.add(character)

    return distinct_characters


def count_characters(polymer: str, distinct_characters: set[str]) -> dict[str, int]:
    character_count: dict[str, int] = {}

    for character in distinct_characters:
        character_count[character] = polymer.count(character)

    return character_count


def evaluate_counts(
    polymer: str, distinct_characters: set[str]
) -> tuple[str, int, str, int]:
    most_common_element: str = ""
    most_common_quantity: int = 0
    least_common_element: str = ""
    least_common_quantity: int = 0

    for character, count in count_characters(polymer, distinct_characters).items():
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


if __name__ == "__main__":
    polymer_template, pair_insertion_rules = read_input("input.txt")
    characters: set[str] = get_distinct_characters(
        polymer_template, pair_insertion_rules
    )

    for _ in range(10):
        polymer_template = apply_rules(polymer_template, pair_insertion_rules)

    largest_element, largest_count, smallest_element, smallest_count = evaluate_counts(
        polymer_template, characters
    )

    print(f"Most common element ({largest_element}, {largest_count}).")
    print(f"Least common element ({smallest_element}, {smallest_count}).")
    print(f"Difference = {largest_count - smallest_count}.")
