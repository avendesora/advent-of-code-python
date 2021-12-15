from dataclasses import dataclass
from itertools import chain


@dataclass
class Point2D:
    x: int
    y: int


@dataclass
class Line:
    start: Point2D
    end: Point2D


def read_input(filename: str) -> list[Line]:
    input_lines: list[Line] = []

    with open(filename, "r", encoding="utf-8") as file_lines:
        for file_line in file_lines:
            if len(_clean_line(file_line).strip()) == 0:
                continue

            start, end = _clean_line(file_line).strip().split(" -> ")
            start_x, start_y = [int(value) for value in start.split(",")]
            end_x, end_y = [int(value) for value in end.split(",")]

            # Ignore diagonals and go ahead and sort
            if (
                start_x == end_x
                and start_y > end_y
                or start_x != end_x
                and start_y == end_y
                and start_x > end_x
            ):
                input_lines.append(
                    Line(Point2D(end_x, end_y), Point2D(start_x, start_y))
                )
            elif (
                start_x == end_x
                and start_y < end_y
                or start_x != end_x
                and start_y == end_y
                and start_x < end_x
            ):
                input_lines.append(
                    Line(Point2D(start_x, start_y), Point2D(end_x, end_y))
                )

    return input_lines


def _clean_line(file_line: str) -> str:
    return file_line.replace("\n", "")


def plot_lines(input_lines: list[Line]) -> list[list[int]]:
    line_graph = _initialize_line_graph(input_lines)

    for input_line in input_lines:
        for row_index in range(input_line.start.y, input_line.end.y + 1):
            for column_index in range(input_line.start.x, input_line.end.x + 1):
                line_graph[row_index][column_index] += 1

    return line_graph


def _initialize_line_graph(input_lines: list[Line]) -> list[list[int]]:
    max_x: int = 0
    max_y: int = 0

    for input_line in input_lines:
        if input_line.end.x + 1 > max_x:
            max_x = input_line.end.x + 1

        if input_line.end.y + 1 > max_y:
            max_y = input_line.end.y + 1

    line_graph: list[list[int]] = []

    for _ in range(max_y):
        line_graph.append([0] * max_x)

    return line_graph


def count_intersections(line_graph: list[list[int]]) -> int:
    return len([cell for cell in list(chain.from_iterable(line_graph)) if cell > 1])


if __name__ == "__main__":
    # Part One
    lines = read_input("input.txt")
    plot = plot_lines(lines)
    print(
        f"There are {count_intersections(plot)} points where at least two lines overlap."
    )
