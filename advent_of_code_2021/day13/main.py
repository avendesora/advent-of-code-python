from __future__ import annotations

from enum import Enum
from pathlib import Path

from helpers import Point2D
from helpers import clean_line
from helpers import transpose_2d_array


class Axis(Enum):
    X = "x"
    Y = "y"


def read_input(filename: Path | str) -> tuple[list[Point2D], list[tuple[Axis, int]]]:
    blank_line_found = False
    input_dots: list[Point2D] = []
    input_instructions: list[tuple[Axis, int]] = []

    with open(filename, encoding="utf-8") as lines:
        for line in lines:
            cleaned_line = clean_line(line).strip()

            if len(cleaned_line) == 0:
                blank_line_found = True
                continue

            if not blank_line_found:
                x, y = cleaned_line.split(",")
                input_dots.append(Point2D(int(x), int(y)))
                continue

            instruction, value = cleaned_line.split("=")
            axis = Axis(instruction[-1])
            input_instructions.append((axis, int(value)))

    return input_dots, input_instructions


def initialize_pattern(input_dots: list[Point2D]) -> list[list[bool]]:
    max_x: int = max(dot.x for dot in input_dots)
    max_y: int = max(dot.y for dot in input_dots)
    initial_pattern: list[list[bool]] = []

    for y in range(max_y + 1):
        initial_pattern.append([])

        for _ in range(max_x + 1):
            initial_pattern[y].append(False)

    for dot in input_dots:
        initial_pattern[dot.y][dot.x] = True

    return initial_pattern


def fold_x(pattern_to_fold: list[list[bool]], value: int) -> list[list[bool]]:
    return transpose_2d_array(fold_y(transpose_2d_array(pattern_to_fold), value))


def fold_y(pattern_to_fold: list[list[bool]], value: int) -> list[list[bool]]:
    folded_pattern: list[list[bool]] = []

    for row_index, row in enumerate(pattern_to_fold):
        if row_index >= value:
            break

        folded_pattern.append([])

        for column_index, cell in enumerate(row):
            try:
                cell_value = (
                    cell or pattern_to_fold[value + (value - row_index)][column_index]
                )
            except IndexError:
                cell_value = cell

            folded_pattern[row_index].append(cell_value)

    return folded_pattern


def execute_instruction(
    pattern_to_fold: list[list[bool]], current_instruction: tuple[Axis, int]
) -> list[list[bool]]:
    axis, value = current_instruction

    if axis == Axis.X:
        return fold_x(pattern_to_fold, value)

    return fold_y(pattern_to_fold, value)


def printable_pattern(
    pattern_to_print: list[list[bool]], false_character: str = "."
) -> str:
    pattern_string: str = ""

    for row in pattern_to_print:
        pattern_string += "".join("#" if cell else false_character for cell in row)
        pattern_string += "\n"

    return pattern_string


def count_visible_dots(current_pattern: list[list[bool]]) -> int:
    return sum(row.count(True) for row in current_pattern)


if __name__ == "__main__":
    # Part One
    dots, instructions = read_input("input.txt")
    pattern: list[list[bool]] = initialize_pattern(dots)

    for instruction in instructions[:1]:
        pattern = execute_instruction(pattern, instruction)

    print(f"There are currently {count_visible_dots(pattern)} dots visible.")

    # Part Two
    dots, instructions = read_input("input.txt")
    pattern = initialize_pattern(dots)

    for instruction in instructions:
        pattern = execute_instruction(pattern, instruction)

    print(printable_pattern(pattern, " "))
