from __future__ import annotations

import string
from contextlib import suppress
from typing import TYPE_CHECKING

from helpers import read_input_as_string_array
from helpers.logger import get_logger
from helpers.simple_dijkstra import WeightedGraph
from helpers.simple_dijkstra import get_weighted_graph

if TYPE_CHECKING:
    from pathlib import Path


LOGGER = get_logger("2022-day-12")


def read_input(filename: Path | str) -> list[list[str]]:
    return [list(line) for line in read_input_as_string_array(filename)]


def get_start_and_end(grid: list[list[str]]) -> tuple[int, int]:
    row_length = len(grid[0])
    start_index = -1
    end_index = -1

    for row_index, row in enumerate(grid):
        for column_index, cell in enumerate(row):
            if start_index > -1 and end_index > -1:
                break

            if cell == "S":
                start_index = row_index * row_length + column_index
                continue

            if cell == "E":
                end_index = row_index * row_length + column_index
                continue

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
                cell,
                row[column_index - 1],
            ):
                edges.append((current_cell, current_cell - 1, 1))

            if row_index > 0 and can_move(
                cell,
                input_data[row_index - 1][column_index],
            ):
                edges.append((current_cell, current_cell - row_length, 1))

            with suppress(IndexError):
                if can_move(cell, row[column_index + 1]):
                    edges.append((current_cell, current_cell + 1, 1))

            with suppress(IndexError):
                if can_move(cell, input_data[row_index + 1][column_index]):
                    edges.append((current_cell, current_cell + row_length, 1))

    return edges


def get_graph(input_data: list[list[str]]) -> WeightedGraph:
    return get_weighted_graph(
        get_edges(input_data),
        len(input_data[0]) * len(input_data),
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
                graph.get_total_least_weight(start_index, end_index),
            )

    return min(all_path_lengths)


if __name__ == "__main__":
    day12_input = read_input("input.txt")

    weighted_graph = get_graph(day12_input)
    start, end = get_start_and_end(day12_input)

    LOGGER.info(part_one(weighted_graph, start, end))
    LOGGER.info(part_two(weighted_graph, end, day12_input))
