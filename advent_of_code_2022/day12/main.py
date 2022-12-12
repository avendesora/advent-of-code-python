from __future__ import annotations

import string
from contextlib import suppress
from pathlib import Path

from helpers import read_input_as_string_array
from helpers.simple_djikstra import WeightedGraph
from helpers.simple_djikstra import get_weighted_graph


def read_input(filename: Path | str) -> list[list[str]]:
    return [list(line) for line in read_input_as_string_array(filename)]


def get_start_and_end(grid: list[list[str]]) -> tuple[int, int]:
    start_row = -1
    start_column = -1
    end_row = -1
    end_column = -1

    for row_index, row in enumerate(grid):
        for column_index, cell in enumerate(row):
            if cell == "S":
                start_row = row_index
                start_column = column_index
                continue

            if cell == "E":
                end_row = row_index
                end_column = column_index
                continue

    row_length = len(grid[0])
    start_index = start_row * row_length + start_column
    end_index = end_row * row_length + end_column

    return start_index, end_index


def can_move(current_cell: str, next_cell: str) -> bool:
    current_lookup = (
        "a" if current_cell == "S" else "z" if current_cell == "E" else current_cell
    )
    next_lookup = "a" if next_cell == "S" else "z" if next_cell == "E" else next_cell

    return (
        string.ascii_lowercase.index(next_lookup)
        <= string.ascii_lowercase.index(current_lookup) + 1
    )


def get_edges(input_data: list[list[str]]) -> list[tuple[int, int, int]]:
    edges: list[tuple[int, int, int]] = []
    row_length = len(input_data[0])

    for row_index, row in enumerate(input_data):
        for column_index, cell in enumerate(row):
            current_cell: int = row_index * row_length + column_index

            if column_index > 0 and can_move(
                cell, input_data[row_index][column_index - 1]
            ):
                edges.append((current_cell, current_cell - 1, 1))

            if row_index > 0 and can_move(
                cell, input_data[row_index - 1][column_index]
            ):
                edges.append((current_cell, current_cell - row_length, 1))

            with suppress(IndexError):
                if can_move(cell, input_data[row_index][column_index + 1]):
                    edges.append((current_cell, current_cell + 1, 1))

            with suppress(IndexError):
                if can_move(cell, input_data[row_index + 1][column_index]):
                    edges.append((current_cell, current_cell + row_length, 1))

    return edges


def get_graph(input_data: list[list[str]]) -> WeightedGraph:
    return get_weighted_graph(
        get_edges(input_data), len(input_data[0]) * len(input_data)
    )


def part_one(graph: WeightedGraph, start_index: int, end_index: int) -> int:
    return graph.get_total_least_weight(start_index, end_index)


def part_two(graph: WeightedGraph, end_index: int, input_data: list[list[str]]) -> int:
    all_starts: list[int] = []

    for row_index, row in enumerate(input_data):
        all_starts.extend(
            row_index * len(input_data[0]) + column_index
            for column_index, cell in enumerate(row)
            if cell == "a"
        )

    all_path_lengths = []

    for start_index in all_starts:
        with suppress(KeyError):  # maybe not all "a" cells have a path to "E"
            all_path_lengths.append(
                graph.get_total_least_weight(start_index, end_index)
            )

    return min(all_path_lengths)


if __name__ == "__main__":
    day12_input = read_input("input.txt")

    weighted_graph = get_graph(day12_input)
    start, end = get_start_and_end(day12_input)

    print(part_one(weighted_graph, start, end))
    print(part_two(weighted_graph, end, day12_input))