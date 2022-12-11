from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2021.day12.main import find_valid_paths
from advent_of_code_2021.day12.main import make_graph
from advent_of_code_2021.day12.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_day_12_read_input(sample_data1: list[tuple[str, ...]]) -> None:
    sample_input = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert sample_input == sample_data1


def test_day_12_part_one(
    sample_data1: list[tuple[str, ...]],
    sample_data2: list[tuple[str, ...]],
    sample_data3: list[tuple[str, ...]],
    valid_paths1: set[str],
    valid_paths2: set[str],
) -> None:
    paths1 = find_valid_paths(make_graph(sample_data1))
    path_strings1 = {", ".join(path) for path in paths1}
    assert path_strings1 == valid_paths1

    paths2 = find_valid_paths(make_graph(sample_data2))
    path_strings2 = {", ".join(path) for path in paths2}
    assert path_strings2 == valid_paths2

    paths3 = find_valid_paths(make_graph(sample_data3))
    assert len(paths3) == 226


def test_day_12_part_two(
    sample_data1: list[tuple[str, ...]],
    sample_data2: list[tuple[str, ...]],
    sample_data3: list[tuple[str, ...]],
    valid_paths1b: set[str],
) -> None:
    paths1 = find_valid_paths(make_graph(sample_data1), 2)
    path_strings1 = {", ".join(path) for path in paths1}
    assert path_strings1 == valid_paths1b

    paths2 = find_valid_paths(make_graph(sample_data2), 2)
    assert len(paths2) == 103

    paths3 = find_valid_paths(make_graph(sample_data3), 2)
    assert len(paths3) == 3509
