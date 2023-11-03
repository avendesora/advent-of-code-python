from __future__ import annotations

import itertools
from contextlib import suppress

from helpers import read_input_as_2d_int_array
from helpers.logger import get_logger
from helpers.simple_dijkstra import WeightedGraph
from helpers.simple_dijkstra import get_weighted_graph

LOGGER = get_logger("2021-day-15")


def get_edges(risk_levels: list[list[int]]) -> list[tuple[int, int, int]]:
    edges: list[tuple[int, int, int]] = []
    row_length = len(risk_levels[0])

    for row_index, row in enumerate(risk_levels):
        for column_index, _ in enumerate(row):
            current_cell: int = row_index * row_length + column_index

            if column_index > 0:
                edges.append(
                    (
                        current_cell,
                        current_cell - 1,
                        risk_levels[row_index][column_index - 1],
                    ),
                )

            if row_index > 0:
                edges.append(
                    (
                        current_cell,
                        current_cell - row_length,
                        risk_levels[row_index - 1][column_index],
                    ),
                )

            with suppress(IndexError):
                edges.append(
                    (
                        current_cell,
                        current_cell + 1,
                        risk_levels[row_index][column_index + 1],
                    ),
                )

            with suppress(IndexError):
                edges.append(
                    (
                        current_cell,
                        current_cell + row_length,
                        risk_levels[row_index + 1][column_index],
                    ),
                )

    return edges


def increase_risk(risk_levels: list[list[int]]) -> list[list[int]]:
    increased_risk_levels: list[list[int]] = []

    for row in risk_levels:
        new_row: list[int] = [0] * len(row)

        for column_index, cell in enumerate(row):
            new_row[column_index] = cell + 1 if cell < 9 else 1

        increased_risk_levels.append(new_row)

    return increased_risk_levels


def get_full_risk_levels(risk_levels: list[list[int]]) -> list[list[int]]:
    risk_levels_list: list[list[list[int]]] = [risk_levels]
    risk_levels_list.extend(
        increase_risk(risk_levels_list[index]) for index in range(9)
    )
    full_risk_levels: list[list[int]] = []

    for row_increase_index, row_index in itertools.product(
        range(5),
        range(len(risk_levels)),
    ):
        new_row: list[int] = []

        for column_increase_index in range(5):
            increase_level: int = row_increase_index + column_increase_index
            new_row.extend(
                risk_levels_list[increase_level][row_index][column_index]
                for column_index in range(len(risk_levels[0]))
            )

        full_risk_levels.append(new_row)

    return full_risk_levels


if __name__ == "__main__":
    input_array: list[list[int]] = read_input_as_2d_int_array("input.txt")
    number_of_vertices = len(input_array) * len(input_array[0])

    # Part One
    risk_graph: WeightedGraph = get_weighted_graph(
        get_edges(input_array),
        number_of_vertices,
    )

    LOGGER.info("The total least risk is %d.", risk_graph.get_total_least_weight())

    # Part Two
    full_input_array: list[list[int]] = get_full_risk_levels(input_array)
    full_risk_graph: WeightedGraph = get_weighted_graph(
        get_edges(full_input_array),
        number_of_vertices * 25,
    )

    LOGGER.info(
        "The full total least risk is %d.",
        full_risk_graph.get_total_least_weight(),
    )
