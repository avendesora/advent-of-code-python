from __future__ import annotations

import itertools
from contextlib import suppress
from dataclasses import dataclass
from heapq import heappop
from heapq import heappush

from helpers import read_input_as_2d_int_array


@dataclass
class Node:
    vertex: int
    risk: int

    def __lt__(self: Node, other: Node) -> bool:
        return self.risk < other.risk


class RiskGraph:
    def __init__(self: RiskGraph, vertex_count: int = 0) -> None:
        self._edges: list[list[dict[str, int]]] = [[] for _ in range(vertex_count)]
        self.vertex_count = vertex_count

    def add_edge(self: RiskGraph, start: int, end: int, risk: int) -> None:
        edge: dict[str, int] = {
            "start": start,
            "end": end,
            "risk": risk,
        }
        self._edges[edge["start"]].append(edge)

    def _edges_for_index(self: RiskGraph, index: int) -> list[dict[str, int]]:
        return self._edges[index]

    def _find_shortest_path(self: RiskGraph, start: int) -> dict[int, dict[str, int]]:
        risks: list[int | None] = [None] * self.vertex_count
        risks[start] = 0
        paths: dict[int, dict[str, int]] = {}
        priority_queue: list[Node] = []
        heappush(priority_queue, Node(start, 0))

        while priority_queue:
            start = heappop(priority_queue).vertex
            risk_start: int = risks[start] or 0

            for weighted_edge in self._edges_for_index(start):
                risk_end: int | None = risks[weighted_edge["end"]]

                if risk_end is None or risk_end > weighted_edge["risk"] + risk_start:
                    risks[weighted_edge["end"]] = weighted_edge["risk"] + risk_start
                    paths[weighted_edge["end"]] = weighted_edge
                    heappush(
                        priority_queue,
                        Node(weighted_edge["end"], weighted_edge["risk"] + risk_start),
                    )

        return paths

    def get_total_least_risk(self: RiskGraph) -> int:
        shortest_path = self._find_shortest_path(0)
        edge: dict[str, int] = shortest_path[self.vertex_count - 1]
        total_risk = edge["risk"]

        while edge["start"] != 0:
            edge = shortest_path[edge["start"]]
            total_risk += edge["risk"]

        return total_risk


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
                    )
                )

            if row_index > 0:
                edges.append(
                    (
                        current_cell,
                        current_cell - row_length,
                        risk_levels[row_index - 1][column_index],
                    )
                )

            with suppress(IndexError):
                edges.append(
                    (
                        current_cell,
                        current_cell + 1,
                        risk_levels[row_index][column_index + 1],
                    )
                )

            with suppress(IndexError):
                edges.append(
                    (
                        current_cell,
                        current_cell + row_length,
                        risk_levels[row_index + 1][column_index],
                    )
                )

    return edges


def get_risk_graph(edges: list[tuple[int, int, int]], vertex_count: int) -> RiskGraph:
    graph = RiskGraph(vertex_count)

    for edge in edges:
        graph.add_edge(edge[0], edge[1], edge[2])

    return graph


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
        range(5), range(len(risk_levels))
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
    risk_graph: RiskGraph = get_risk_graph(get_edges(input_array), number_of_vertices)
    print(f"The total least risk is {risk_graph.get_total_least_risk()}.")

    # Part Two
    full_input_array: list[list[int]] = get_full_risk_levels(input_array)
    full_risk_graph: RiskGraph = get_risk_graph(
        get_edges(full_input_array), number_of_vertices * 25
    )
    print(f"The full total least risk is {full_risk_graph.get_total_least_risk()}.")
