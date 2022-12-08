from dataclasses import dataclass
from pathlib import Path
from typing import Any

from helpers import clean_line


@dataclass
class GraphNode:
    name: str
    connected_nodes: list[Any]


def read_input(filename: Path | str) -> list[tuple[str, ...]]:
    with open(filename, encoding="utf-8") as lines:
        return [tuple(clean_line(line).split("-")) for line in lines]


def make_graph(connections: list[tuple[str, ...]]) -> GraphNode:
    graph_nodes: dict[str, GraphNode] = {}

    for connection in connections:
        graph_node1 = graph_nodes.get(connection[0], GraphNode(connection[0], []))
        graph_node2 = graph_nodes.get(connection[1], GraphNode(connection[1], []))

        graph_node1.connected_nodes.append(graph_node2)
        graph_node2.connected_nodes.append(graph_node1)

        graph_nodes[connection[0]] = graph_node1
        graph_nodes[connection[1]] = graph_node2

    return graph_nodes.get("start", GraphNode("start", []))


def find_valid_paths(
    start: GraphNode, small_cave_visit_max: int = 1
) -> list[list[str]]:
    paths: list[list[str]] = find_paths(start, [], small_cave_visit_max)
    return [path for path in paths if path[0] == "start" and path[-1] == "end"]


def find_paths(
    current_node: GraphNode, current_path: list[str], small_cave_visit_max: int
) -> list[list[str]]:
    current_path.append(current_node.name)

    if current_node.name == "end":
        return [current_path]

    visits = current_path.count(current_node.name)

    if _is_small_cave(current_node) and visits >= small_cave_visit_max:
        small_cave_visit_max = 1

    paths: list[list[str]] = []

    for connection in current_node.connected_nodes:
        connection_visits = current_path.count(connection.name)

        if connection.name == "start" and connection_visits > 0:
            continue

        if _is_small_cave(connection) and connection_visits >= small_cave_visit_max:
            small_cave_visit_max = 1
            continue

        paths.extend(find_paths(connection, current_path.copy(), small_cave_visit_max))

    if not paths:
        paths.append(current_path)

    return paths


def _is_small_cave(node: GraphNode) -> bool:
    return node.name.lower() == node.name


if __name__ == "__main__":
    initial_connections = read_input("input.txt")
    graph = make_graph(initial_connections)

    # Part One
    valid_paths = find_valid_paths(graph)
    print(f"There are {len(valid_paths)} valid paths through this cave system.")

    # Part Two
    valid_paths2 = find_valid_paths(graph, 2)
    print(
        f"There are {len(valid_paths2)} valid paths through this cave system with "
        f"visiting small caves twice at most."
    )
