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


SEGMENT_MAPPING: set[str] = {"a", "b", "c", "d", "e", "f", "g"}


def get_segment_mappings(number_of_segments: int) -> list[set[str]]:
    return [SEGMENT_MAPPING.copy() for _ in range(number_of_segments)]


def get_digit_mappings(number_of_digits: int) -> list[str]:
    return ["" for _ in range(number_of_digits)]


def update_digit_mappings(
    signal_pattern_entry: list[str],
    digit_mappings: list[str],
) -> tuple[list[str], list[str]]:
    two_three_five = []
    zero_six_nine = []

    for signal_pattern_value in signal_pattern_entry:
        if len(signal_pattern_value) == 2:
            digit_mappings[1] = signal_pattern_value
            continue

        if len(signal_pattern_value) == 3:
            digit_mappings[7] = signal_pattern_value
            continue

        if len(signal_pattern_value) == 4:
            digit_mappings[4] = signal_pattern_value
            continue

        if len(signal_pattern_value) == 5:
            two_three_five.append(signal_pattern_value)
            continue

        if len(signal_pattern_value) == 6:
            zero_six_nine.append(signal_pattern_value)
            continue

        if len(signal_pattern_value) == 7:
            digit_mappings[8] = signal_pattern_value
            continue

    return two_three_five, zero_six_nine


def update_mappings_for_digit1(
    segment_mappings: list[set[str]],
    digit_mappings: list[str],
) -> None:
    digit_1_set = set(digit_mappings[1])
    segment_mappings[0] = segment_mappings[0].symmetric_difference(digit_1_set)
    segment_mappings[1] = segment_mappings[1].symmetric_difference(digit_1_set)
    segment_mappings[2] = digit_1_set.copy()
    segment_mappings[3] = segment_mappings[3].symmetric_difference(digit_1_set)
    segment_mappings[4] = segment_mappings[4].symmetric_difference(digit_1_set)
    segment_mappings[5] = digit_1_set.copy()
    segment_mappings[6] = segment_mappings[6].symmetric_difference(digit_1_set)


def update_mappings_for_digit7(
    segment_mappings: list[set[str]],
    digit_mappings: list[str],
) -> None:
    character_set = set(digit_mappings[7]).symmetric_difference(segment_mappings[2])
    segment_mappings[0] = character_set.copy()
    character = character_set.pop()
    segment_mappings[1].discard(character)
    segment_mappings[3].discard(character)
    segment_mappings[4].discard(character)
    segment_mappings[6].discard(character)


def update_mappings_for_digit4(
    segment_mappings: list[set[str]],
    digit_mappings: list[str],
) -> None:
    character_set = set(digit_mappings[4]).symmetric_difference(segment_mappings[2])
    segment_mappings[1] = character_set.copy()
    segment_mappings[3] = character_set.copy()
    segment_mappings[4] = segment_mappings[4].symmetric_difference(character_set)
    segment_mappings[6] = segment_mappings[6].symmetric_difference(character_set)


def update_mappings_for_digit9(
    segment_mappings: list[set[str]],
    digit_mappings: list[str],
    zero_six_nine: list[str],
) -> None:
    for signal_pattern_value in zero_six_nine:
        search_set = (
            segment_mappings[0].union(segment_mappings[1]).union(segment_mappings[2])
        )
        character_set = set(signal_pattern_value).symmetric_difference(search_set)

        if len(character_set) != 1:
            continue

        segment_mappings[6] = character_set.copy()
        segment_mappings[4].discard(character_set.pop())
        digit_mappings[9] = signal_pattern_value
        zero_six_nine.remove(digit_mappings[9])
        break


def update_mappings_for_digit0(
    segment_mappings: list[set[str]],
    digit_mappings: list[str],
    zero_six_nine: list[str],
) -> None:
    for signal_pattern_value in zero_six_nine:
        search_set = segment_mappings[2].union(segment_mappings[4])
        character_set = set(signal_pattern_value).symmetric_difference(search_set)

        if len(character_set) != 3:
            continue

        segment_mappings[1] = segment_mappings[1].intersection(character_set)
        segment_mappings[3] = segment_mappings[3].symmetric_difference(
            segment_mappings[1]
        )
        digit_mappings[0] = signal_pattern_value
        zero_six_nine.remove(digit_mappings[0])
        break


def update_mappings_for_digit6(
    segment_mappings: list[set[str]],
    digit_mappings: list[str],
    zero_six_nine: list[str],
) -> None:
    digit_mappings[6] = zero_six_nine.pop(0)
    segment_mappings[5] = segment_mappings[5].intersection(set(digit_mappings[6]))
    segment_mappings[2] = segment_mappings[2].symmetric_difference(segment_mappings[5])


def update_mappings_for_digits_2_3_5(
    segment_mappings: list[set[str]],
    digit_mappings: list[str],
    two_three_five: list[str],
) -> None:
    for signal_pattern_value in two_three_five:
        # Digit 3
        if (
            len(set(signal_pattern_value).symmetric_difference(set(digit_mappings[1])))
            == 3
        ):
            digit_mappings[3] = signal_pattern_value
            continue

        # Digit 5
        if list(segment_mappings[1])[0] in signal_pattern_value:
            digit_mappings[5] = signal_pattern_value
            continue

        # Digit 2
        if list(segment_mappings[4])[0] in signal_pattern_value:
            digit_mappings[2] = signal_pattern_value
            continue


def get_digits(signal_pattern_entry: list[str]) -> list[str]:
    segment_mappings = get_segment_mappings(7)
    digit_mappings = get_digit_mappings(10)

    two_three_five, zero_six_nine = update_digit_mappings(
        signal_pattern_entry,
        digit_mappings,
    )

    update_mappings_for_digit1(segment_mappings, digit_mappings)
    update_mappings_for_digit7(segment_mappings, digit_mappings)
    update_mappings_for_digit4(segment_mappings, digit_mappings)
    update_mappings_for_digit9(segment_mappings, digit_mappings, zero_six_nine)
    update_mappings_for_digit0(segment_mappings, digit_mappings, zero_six_nine)
    update_mappings_for_digit6(segment_mappings, digit_mappings, zero_six_nine)
    update_mappings_for_digits_2_3_5(segment_mappings, digit_mappings, two_three_five)

    return ["".join(sorted(digit_mapping)) for digit_mapping in digit_mappings]


def part_one(output_values: list[list[str]]) -> int:
    count1478: int = 0

    for output_value in output_values:
        for value in output_value:
            if len(value) in {2, 3, 4, 7}:
                count1478 += 1

    return count1478


def part_two(
    signal_patterns: list[list[str]],
    output_values: list[list[str]],
) -> int:
    total = 0

    for index, signal_pattern in enumerate(signal_patterns):
        digits = get_digits(signal_pattern)
        output_value = output_values[index]

        digit_string = ""

        for value in output_value:
            sorted_value = "".join(sorted(value))
            digit_string += str(digits.index(sorted_value))

        total += int(digit_string)

    return total


if __name__ == "__main__":
    signal_patterns_input, output_values_input = read_input("input.txt")
    part_one_total = part_one(output_values_input)
    print(f"The digits 1, 4, 7, or 8 appear {part_one_total} times.")
    part_two_total = part_two(signal_patterns_input, output_values_input)
    print(f"The total value is {part_two_total}.")
