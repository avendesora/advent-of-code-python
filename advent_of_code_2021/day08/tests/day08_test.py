from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2021.day08.main import part_one
from advent_of_code_2021.day08.main import part_two
from advent_of_code_2021.day08.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input(
    signal_patterns: list[list[str]],
    output_values: list[list[str]],
) -> None:
    signal_patterns_input, output_values_input = read_input(
        CURRENT_DIRECTORY / "sample_input.txt"
    )
    assert signal_patterns_input == signal_patterns
    assert output_values_input == output_values


def test_part_one(output_values: list[list[str]]) -> None:
    assert part_one(output_values) == 26


def test_part_two(
    signal_patterns: list[list[str]],
    output_values: list[list[str]],
) -> None:
    assert part_two(signal_patterns, output_values) == 61229
