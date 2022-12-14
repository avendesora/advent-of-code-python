from __future__ import annotations

import itertools
from pathlib import Path

from helpers import Point2D
from helpers import read_input_as_string_array


def read_input(filename: Path | str) -> tuple[list[list[Point2D]], int, int, int]:
    paths: list[list[Point2D]] = []
    x_values: set(int) = set()
    y_values: set(int) = set()

    for line in read_input_as_string_array(filename):
        path: list[Point2D] = []

        for point in line.split(" -> "):
            x, y = (int(value) for value in point.split(","))
            path.append(Point2D(x, y))
            x_values.add(x)
            y_values.add(y)

        paths.append(path)

    return paths, min(x_values), max(x_values), max(y_values)


def draw_grid(
    input_data: list[list[Point2D]],
    min_x: int,
    max_x: int,
    max_y: int,
) -> list[list[str]]:
    grid: list[list[str]] = [
        ["." for _ in range(min_x, max_x + 1)] for _ in range(max_y + 1)
    ]

    for path in input_data:
        for index, point in enumerate(path):
            try:
                next_point = path[index + 1]
            except IndexError:
                break

            if point.x == next_point.x:
                x = point.x - min_x

                if point.y < next_point.y:
                    for y in range(point.y, next_point.y + 1):
                        grid[y][x] = "#"
                else:
                    for y in range(next_point.y, point.y + 1):
                        grid[y][x] = "#"
            elif point.x < next_point.x:
                for x in range(point.x - min_x, next_point.x - min_x + 1):
                    grid[point.y][x] = "#"
            else:
                for x in range(next_point.x - min_x, point.x - min_x + 1):
                    grid[point.y][x] = "#"

    return grid


def pour_sand(grid: list[list[str]], x_offset: int) -> int:
    sand_count = 0
    current_sand = None

    try:
        while True:
            if current_sand is None:
                current_sand = Point2D(500, 0)
                sand_count += 1
                continue

            down = grid[current_sand.y + 1][current_sand.x - x_offset]

            if down == ".":
                current_sand.y += 1
                continue

            down_and_left = grid[current_sand.y + 1][current_sand.x - x_offset - 1]

            if down_and_left == ".":
                current_sand.y += 1
                current_sand.x -= 1
                continue

            down_and_right = grid[current_sand.y + 1][current_sand.x - x_offset + 1]

            if down_and_right == ".":
                current_sand.y += 1
                current_sand.x += 1
                continue

            grid[current_sand.y][current_sand.x - x_offset] = "o"

            if current_sand.y == 0 and current_sand.x == 500:
                break

            current_sand = None
    except IndexError:
        sand_count -= 1

    return sand_count


def part_one(grid: list[list[str]], x_offset: int) -> int:
    return pour_sand(grid, x_offset)


def part_two(grid: list[list[str]], x_offset: int) -> int:
    row_length = len(grid[0])
    padding = len(grid)
    x_offset -= padding

    for row, _ in itertools.product(grid, range(padding)):
        row.insert(0, ".")
        row.append(".")

    grid.extend(
        (
            ["." for _ in range(padding + row_length + padding)],
            ["#" for _ in range(padding + row_length + padding)],
        )
    )

    return pour_sand(grid, x_offset)


if __name__ == "__main__":
    day14_input, x_min, x_max, y_max = read_input("input.txt")
    grid_input: list[list[str]] = draw_grid(day14_input, x_min, x_max, y_max)
    print(part_one(grid_input, x_min))

    grid_input = draw_grid(day14_input, x_min, x_max, y_max)
    print(part_two(grid_input, x_min))
