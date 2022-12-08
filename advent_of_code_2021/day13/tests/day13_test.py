import os
from pathlib import Path

from advent_of_code_2021.day13.main import Axis
from advent_of_code_2021.day13.main import count_visible_dots
from advent_of_code_2021.day13.main import execute_instruction
from advent_of_code_2021.day13.main import initialize_pattern
from advent_of_code_2021.day13.main import printable_pattern
from advent_of_code_2021.day13.main import read_input
from helpers import Point2D

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_day_13_read_input(
    sample_data: tuple[list[Point2D], list[tuple[Axis, int]]]
) -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == sample_data


def test_initialize_pattern(
    sample_data: tuple[list[Point2D], list[tuple[Axis, int]]],
    initial_pattern: list[list[bool]],
) -> None:
    dots, _ = sample_data
    pattern = initialize_pattern(dots)

    assert pattern == initial_pattern


def test_printable_pattern(
    sample_data: tuple[list[Point2D], list[tuple[Axis, int]]],
    pattern_string: str,
) -> None:
    dots, _ = sample_data
    pattern = initialize_pattern(dots)
    actual_pattern_string = printable_pattern(pattern)

    assert actual_pattern_string == pattern_string


def test_fold_y(
    sample_data: tuple[list[Point2D], list[tuple[Axis, int]]],
    folded_pattern_y: list[list[bool]],
    folded_pattern_y_string: str,
) -> None:
    dots, instructions = sample_data
    pattern = initialize_pattern(dots)
    actual_folded_pattern = execute_instruction(pattern, instructions[0])
    actual_folded_pattern_string = printable_pattern(actual_folded_pattern)

    assert actual_folded_pattern == folded_pattern_y
    assert actual_folded_pattern_string == folded_pattern_y_string


def test_fold_x(
    sample_data: tuple[list[Point2D], list[tuple[Axis, int]]],
    folded_pattern_x: list[list[bool]],
    folded_pattern_x_string: str,
) -> None:
    dots, instructions = sample_data
    pattern = initialize_pattern(dots)
    folded_pattern_y = execute_instruction(pattern, instructions[0])
    actual_folded_pattern_x = execute_instruction(folded_pattern_y, instructions[1])
    actual_folded_pattern_x_string = printable_pattern(actual_folded_pattern_x)

    assert actual_folded_pattern_x == folded_pattern_x
    assert actual_folded_pattern_x_string == folded_pattern_x_string


def test_count_dots(sample_data: tuple[list[Point2D], list[tuple[Axis, int]]]) -> None:
    dots, instructions = sample_data
    pattern = initialize_pattern(dots)
    folded_pattern_y = execute_instruction(pattern, instructions[0])

    assert count_visible_dots(folded_pattern_y) == 17

    folded_pattern_x = execute_instruction(folded_pattern_y, instructions[1])

    assert count_visible_dots(folded_pattern_x) == 16
