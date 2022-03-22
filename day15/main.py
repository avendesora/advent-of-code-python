from __future__ import annotations

from contextlib import suppress
from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Optional

from helpers import read_input_as_2d_int_array


@dataclass
class Node:
    vertex: int
    risk: int

    def __lt__(self, other: Node) -> bool:
        return self.risk < other.risk


class PriorityQueue:
    def __init__(self) -> None:
        self._container: list[Node] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: Node) -> None:
        heappush(self._container, item)

    def pop(self) -> Node:
        return heappop(self._container)


@dataclass
class Edge:
    start: int
    end: int
    risk: int

    def reversed(self) -> Edge:
        return Edge(self.end, self.start, self.risk)

    def __lt__(self, other: Edge) -> bool:
        return self.risk < other.risk


class Graph:
    def __init__(self, vertices: list[str]) -> None:
        self._vertices: list[str] = vertices
        self._edges: list[list[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)

    def add_edge(self, first: str, second: str, weight: int) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        edge: Edge = Edge(u, v, weight)
        self._edges[edge.start].append(edge)

    def index_of(self, vertex: str) -> int:
        return self._vertices.index(vertex)

    def edges_for_index(self, index: int) -> list[Edge]:
        return self._edges[index]


def read_input(filename: str) -> tuple[list[tuple[str, str, int]], list[str]]:
    input_array: list[list[int]] = read_input_as_2d_int_array(filename)
    vertices: list[str] = []
    edges: list[tuple[str, str, int]] = []

    for row_index, row in enumerate(input_array):
        for column_index, _ in enumerate(row):
            current_cell_name: str = f"{row_index}-{column_index}"
            vertices.append(current_cell_name)

            with suppress(IndexError):
                if column_index > 0:
                    edges.append(
                        (
                            current_cell_name,
                            f"{row_index}-{column_index - 1}",
                            input_array[row_index][column_index - 1],
                        )
                    )

            with suppress(IndexError):
                if row_index > 0:
                    edges.append(
                        (
                            current_cell_name,
                            f"{row_index - 1}-{column_index}",
                            input_array[row_index - 1][column_index],
                        )
                    )

            with suppress(IndexError):
                edges.append(
                    (
                        current_cell_name,
                        f"{row_index}-{column_index + 1}",
                        input_array[row_index][column_index + 1],
                    )
                )

            with suppress(IndexError):
                edges.append(
                    (
                        current_cell_name,
                        f"{row_index + 1}-{column_index}",
                        input_array[row_index + 1][column_index],
                    )
                )

    return edges, vertices


def find_shortest_path(weighted_graph: Graph, root: str) -> dict[int, Edge]:
    start: int = weighted_graph.index_of(root)
    risks: list[Optional[int]] = [None] * weighted_graph.vertex_count
    risks[start] = 0
    paths: dict[int, Edge] = {}
    priority_queue: PriorityQueue = PriorityQueue()
    priority_queue.push(Node(start, 0))

    while not priority_queue.empty:
        start = priority_queue.pop().vertex
        risk_start: int = risks[start] or 0

        for weighted_edge in weighted_graph.edges_for_index(start):
            risk_end: Optional[int] = risks[weighted_edge.end]

            if risk_end is None or risk_end > weighted_edge.risk + risk_start:
                risks[weighted_edge.end] = weighted_edge.risk + risk_start
                paths[weighted_edge.end] = weighted_edge
                priority_queue.push(
                    Node(weighted_edge.end, weighted_edge.risk + risk_start)
                )

    return paths


def path_dict_to_path(start: int, end: int, path_dict: dict[int, Edge]) -> list[Edge]:
    if not path_dict:
        return []

    edge_path: list[Edge] = []
    edge: Edge = path_dict[end]
    edge_path.append(edge)

    while edge.start != start:
        edge = path_dict[edge.start]
        edge_path.append(edge)

    return list(reversed(edge_path))


def get_risk_graph(edges: list[tuple[str, str, int]], vertices: list[str]) -> Graph:
    graph = Graph(vertices)

    for edge in edges:
        graph.add_edge(edge[0], edge[1], edge[2])

    return graph


def get_total_least_risk(graph: Graph, vertices: list[str]) -> int:
    start = vertices[0]
    end = vertices[-1]

    shortest_path = path_dict_to_path(
        graph.index_of(start),
        graph.index_of(end),
        find_shortest_path(graph, start),
    )

    return sum(edge.risk for edge in shortest_path)


if __name__ == "__main__":
    # Part One
    input_edges, input_vertices = read_input("input.txt")

    risk_graph = get_risk_graph(input_edges, input_vertices)
    total_least_risk = get_total_least_risk(risk_graph, input_vertices)

    print(f"The total least risk is {total_least_risk}.")
