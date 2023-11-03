from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2022.day12.main import get_graph
from advent_of_code_2022.day12.main import get_start_and_end
from advent_of_code_2022.day12.main import part_one
from advent_of_code_2022.day12.main import part_two
from advent_of_code_2022.day12.main import read_input

CURRENT_DIRECTORY = Path(Path(os.path.realpath(__file__)).parent)


def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == [
        ["S", "a", "b", "q", "p", "o", "n", "m"],
        ["a", "b", "c", "r", "y", "x", "x", "l"],
        ["a", "c", "c", "s", "z", "E", "x", "k"],
        ["a", "c", "c", "t", "u", "v", "w", "j"],
        ["a", "b", "d", "e", "f", "g", "h", "i"],
    ]


def test_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    graph = get_graph(input_data)
    start, end = get_start_and_end(input_data)
    assert part_one(graph, start, end) == 31


def test_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    graph = get_graph(input_data)
    _, end = get_start_and_end(input_data)
    assert part_two(graph, end, input_data) == 29
