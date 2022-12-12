from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop
from heapq import heappush


@dataclass
class Node:
    vertex: int
    weight: int

    def __lt__(self: Node, other: object) -> bool:
        if not isinstance(other, Node):
            raise NotImplementedError

        return self.weight < other.weight

    def __eq__(self: Node, other: object) -> bool:
        if not isinstance(other, Node):
            raise NotImplementedError

        return self.weight == other.weight


class WeightedGraph:
    def __init__(self: WeightedGraph, vertex_count: int = 0) -> None:
        self._edges: list[list[dict[str, int]]] = [[] for _ in range(vertex_count)]
        self.vertex_count = vertex_count

    def add_edge(self: WeightedGraph, start: int, end: int, weight: int) -> None:
        edge: dict[str, int] = {
            "start": start,
            "end": end,
            "weight": weight,
        }
        self._edges[edge["start"]].append(edge)

    def _edges_for_index(self: WeightedGraph, index: int) -> list[dict[str, int]]:
        return self._edges[index]

    def _find_shortest_path(
        self: WeightedGraph, start: int
    ) -> dict[int, dict[str, int]]:
        weights: list[int | None] = [None] * self.vertex_count
        weights[start] = 0
        paths: dict[int, dict[str, int]] = {}
        priority_queue: list[Node] = []
        heappush(priority_queue, Node(start, 0))

        while priority_queue:
            start = heappop(priority_queue).vertex
            weight_start: int = weights[start] or 0

            for weighted_edge in self._edges_for_index(start):
                weight_end: int | None = weights[weighted_edge["end"]]

                if (
                    weight_end is None
                    or weight_end > weighted_edge["weight"] + weight_start
                ):
                    weights[weighted_edge["end"]] = (
                        weighted_edge["weight"] + weight_start
                    )
                    paths[weighted_edge["end"]] = weighted_edge
                    heappush(
                        priority_queue,
                        Node(
                            weighted_edge["end"], weighted_edge["weight"] + weight_start
                        ),
                    )

        return paths

    def get_total_least_weight(
        self: WeightedGraph, start: int = 0, end: int | None = None
    ) -> int:
        shortest_path = self._find_shortest_path(start)
        edge: dict[str, int] = shortest_path[end or (self.vertex_count - 1)]
        total_weight = edge["weight"]

        while edge["start"] != start:
            edge = shortest_path[edge["start"]]
            total_weight += edge["weight"]

        return total_weight


def get_weighted_graph(
    edges: list[tuple[int, int, int]], vertex_count: int
) -> WeightedGraph:
    graph = WeightedGraph(vertex_count)

    for edge in edges:
        graph.add_edge(edge[0], edge[1], edge[2])

    return graph
