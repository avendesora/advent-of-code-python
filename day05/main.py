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

            # 45 degree diagonals
            if _is_diagonal(start_x, start_y, end_x, end_y):
                input_lines.append(
                    Line(Point2D(start_x, start_y), Point2D(end_x, end_y))
                )

    return input_lines


def _clean_line(file_line: str) -> str:
    return file_line.replace("\n", "")


def _is_diagonal(start_x, start_y, end_x, end_y):
    return abs(start_x - end_x) == abs(start_y - end_y)


def plot_horizontal_and_vertical_lines(input_lines: list[Line]) -> list[list[int]]:
    line_graph = _initialize_line_graph(input_lines)

    for input_line in input_lines:
        if _is_diagonal(
            input_line.start.x, input_line.start.y, input_line.end.x, input_line.end.y
        ):
            continue

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


def plot_diagonal_lines(
    input_lines: list[Line], line_graph: list[list[int]]
) -> list[list[int]]:
    for input_line in input_lines:
        if not _is_diagonal(
            input_line.start.x, input_line.start.y, input_line.end.x, input_line.end.y
        ):
            continue

        x_increment, start_x, end_x = _get_increment_start_and_end(
            input_line.start.x, input_line.end.x
        )
        y_increment, start_y, end_y = _get_increment_start_and_end(
            input_line.start.y, input_line.end.y
        )
        x_coordinates = list(range(start_x, end_x, x_increment))

        for index, row_index in enumerate(range(start_y, end_y, y_increment)):
            column_index = x_coordinates[index]
            line_graph[row_index][column_index] += 1

    return line_graph


def _get_increment_start_and_end(start: int, end: int) -> tuple[int, int, int]:
    return (1, start, end + 1) if start < end else (-1, start, end - 1)


def count_intersections(line_graph: list[list[int]]) -> int:
    return len([cell for cell in list(chain.from_iterable(line_graph)) if cell > 1])


if __name__ == "__main__":
    # Part One
    lines = read_input("input.txt")
    plot = plot_horizontal_and_vertical_lines(lines)

    for plot_line in plot:
        print(plot_line)

    print(
        f"There are {count_intersections(plot)} points where at least two lines overlap."
    )

    # Part Two
    plot2 = plot_diagonal_lines(lines, plot)

    for plot_line in plot2:
        print(plot_line)

    print(
        f"There are {count_intersections(plot2)} points where at least two lines overlap."
    )
