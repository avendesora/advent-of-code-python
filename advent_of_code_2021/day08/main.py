from pathlib import Path

from helpers import clean_line


def read_input(filename: Path | str) -> tuple[list[list[str]], list[list[str]]]:
    input_signal_patterns: list[list[str]] = []
    input_output_values: list[list[str]] = []

    with open(filename, encoding="utf-8") as file_lines:
        for file_line in file_lines:
            clean_file_line = clean_line(file_line).strip()

            if len(clean_file_line) == 0:
                continue

            raw_signal_patterns, raw_output_values = clean_file_line.split(" | ")
            input_signal_patterns.append(raw_signal_patterns.split(" "))
            input_output_values.append(raw_output_values.split(" "))

    return input_signal_patterns, input_output_values


def get_digits(signal_pattern_entry: list[str]) -> list[str]:
    segment_1_mappings: set[str] = {"a", "b", "c", "d", "e", "f", "g"}
    segment_2_mappings: set[str] = {"a", "b", "c", "d", "e", "f", "g"}
    segment_3_mappings: set[str] = {"a", "b", "c", "d", "e", "f", "g"}
    segment_4_mappings: set[str] = {"a", "b", "c", "d", "e", "f", "g"}
    segment_5_mappings: set[str] = {"a", "b", "c", "d", "e", "f", "g"}
    segment_6_mappings: set[str] = {"a", "b", "c", "d", "e", "f", "g"}
    segment_7_mappings: set[str] = {"a", "b", "c", "d", "e", "f", "g"}

    digit_0_mapping: str = ""
    digit_1_mapping: str = ""
    digit_2_mapping: str = ""
    digit_3_mapping: str = ""
    digit_4_mapping: str = ""
    digit_5_mapping: str = ""
    digit_6_mapping: str = ""
    digit_7_mapping: str = ""
    digit_8_mapping: str = ""
    digit_9_mapping: str = ""

    two_three_five = []
    zero_six_nine = []

    for signal_pattern_value in signal_pattern_entry:
        if len(signal_pattern_value) == 2:
            digit_1_mapping = signal_pattern_value
            continue

        if len(signal_pattern_value) == 3:
            digit_7_mapping = signal_pattern_value
            continue

        if len(signal_pattern_value) == 4:
            digit_4_mapping = signal_pattern_value
            continue

        if len(signal_pattern_value) == 5:
            two_three_five.append(signal_pattern_value)
            continue

        if len(signal_pattern_value) == 6:
            zero_six_nine.append(signal_pattern_value)
            continue

        if len(signal_pattern_value) == 7:
            digit_8_mapping = signal_pattern_value
            continue

    # Digit 1
    digit_1_set = set(digit_1_mapping)
    segment_1_mappings = segment_1_mappings.symmetric_difference(digit_1_set)
    segment_2_mappings = segment_2_mappings.symmetric_difference(digit_1_set)
    segment_3_mappings = digit_1_set.copy()
    segment_4_mappings = segment_4_mappings.symmetric_difference(digit_1_set)
    segment_5_mappings = segment_5_mappings.symmetric_difference(digit_1_set)
    segment_6_mappings = digit_1_set.copy()
    segment_7_mappings = segment_7_mappings.symmetric_difference(digit_1_set)

    # Digit 7
    character_set = set(digit_7_mapping).symmetric_difference(segment_3_mappings)
    segment_1_mappings = character_set.copy()
    character = character_set.pop()
    segment_2_mappings.discard(character)
    segment_4_mappings.discard(character)
    segment_5_mappings.discard(character)
    segment_7_mappings.discard(character)

    # Digit 4
    character_set = set(digit_4_mapping).symmetric_difference(segment_3_mappings)
    segment_2_mappings = character_set.copy()
    segment_4_mappings = character_set.copy()
    segment_5_mappings = segment_5_mappings.symmetric_difference(character_set)
    segment_7_mappings = segment_7_mappings.symmetric_difference(character_set)

    # Digit 9
    for signal_pattern_value in zero_six_nine:
        search_set = segment_1_mappings.union(segment_2_mappings).union(
            segment_3_mappings
        )
        character_set = set(signal_pattern_value).symmetric_difference(search_set)

        if len(character_set) != 1:
            continue

        segment_7_mappings = character_set.copy()
        segment_5_mappings.discard(character_set.pop())
        digit_9_mapping = signal_pattern_value
        zero_six_nine.remove(digit_9_mapping)
        break

    # Digit 0
    for signal_pattern_value in zero_six_nine:
        search_set = segment_3_mappings.union(segment_5_mappings)
        character_set = set(signal_pattern_value).symmetric_difference(search_set)

        if len(character_set) != 3:
            continue

        segment_2_mappings = segment_2_mappings.intersection(character_set)
        segment_4_mappings = segment_4_mappings.symmetric_difference(segment_2_mappings)
        digit_0_mapping = signal_pattern_value
        zero_six_nine.remove(digit_0_mapping)
        break

    # Digit 6
    digit_6_mapping = zero_six_nine.pop(0)
    segment_6_mappings = segment_6_mappings.intersection(set(digit_6_mapping))
    segment_3_mappings = segment_3_mappings.symmetric_difference(segment_6_mappings)

    for signal_pattern_value in two_three_five:
        # Digit 3
        if (
            len(set(signal_pattern_value).symmetric_difference(set(digit_1_mapping)))
            == 3
        ):
            digit_3_mapping = signal_pattern_value
            continue

        # Digit 5
        if list(segment_2_mappings)[0] in signal_pattern_value:
            digit_5_mapping = signal_pattern_value
            continue

        # Digit 2
        if list(segment_5_mappings)[0] in signal_pattern_value:
            digit_2_mapping = signal_pattern_value
            continue

    return [
        "".join(sorted(digit_0_mapping)),
        "".join(sorted(digit_1_mapping)),
        "".join(sorted(digit_2_mapping)),
        "".join(sorted(digit_3_mapping)),
        "".join(sorted(digit_4_mapping)),
        "".join(sorted(digit_5_mapping)),
        "".join(sorted(digit_6_mapping)),
        "".join(sorted(digit_7_mapping)),
        "".join(sorted(digit_8_mapping)),
        "".join(sorted(digit_9_mapping)),
    ]


if __name__ == "__main__":
    signal_patterns, output_values = read_input("input.txt")

    # Part One
    count1478: int = 0

    for output_value in output_values:
        for value in output_value:
            if len(value) in {2, 3, 4, 7}:
                count1478 += 1

    print(f"The digits 1, 4, 7, or 8 appear {count1478} times.")

    # Part Two
    total = 0

    for index, signal_pattern in enumerate(signal_patterns):
        digits = get_digits(signal_pattern)
        output_value = output_values[index]

        digit_string = ""

        for value in output_value:
            sorted_value = "".join(sorted(value))
            digit_string += str(digits.index(sorted_value))

        total += int(digit_string)

    print(f"The total value is {total}.")
