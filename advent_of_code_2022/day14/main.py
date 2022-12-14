from __future__ import annotations

from contextlib import suppress
from pathlib import Path

from helpers import Point2D
from helpers import read_input_as_string_array


def read_input(filename: Path | str) -> list[list[Point2D]]:
    paths: list[list[Point2D]] = []

    for line in read_input_as_string_array(filename):
        path: list[Point2D] = []

        for point in line.split(" -> "):
            point_x, point_y = point.split(",")
            path.append(Point2D(int(point_x), int(point_y)))

        paths.append(path)

    return paths


def draw_grid(input_data: list[list[Point2D]]) -> tuple[list[list[str]], int]:
    min_x = -1
    max_x = -1
    max_y = -1

    for row in input_data:
        for cell in row:
            if cell.x < min_x or min_x == -1:
                min_x = cell.x

            if cell.x > max_x or max_x == -1:
                max_x = cell.x

            if cell.y > max_y or max_y == -1:
                max_y = cell.y

    grid: list[list[str]] = []

    for _ in range(max_y + 1):
        grid_row: list[str] = []

        for _ in range(min_x, max_x + 1):
            grid_row.append(".")

        grid.append(grid_row)

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
            else:
                if point.x < next_point.x:
                    for x in range(point.x - min_x, next_point.x - min_x + 1):
                        grid[point.y][x] = "#"
                else:
                    for x in range(next_point.x - min_x, point.x - min_x + 1):
                        grid[point.y][x] = "#"

    return grid, min_x


def pour_sand(grid: list[list[str]], x_offset: int) -> int:
    sand_count = 0
    current_sand = None

    with suppress(IndexError):
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

    return sand_count


def part_one(input_data: list[list[Point2D]]) -> int:
    grid, x_offset = draw_grid(input_data)
    sand_count = pour_sand(grid, x_offset)
    return sand_count - 1


def part_two(input_data: list[list[Point2D]]) -> int:
    grid, x_offset = draw_grid(input_data)
    row_length = len(grid[0])
    padding = len(grid)
    x_offset -= padding

    for row in grid:
        for _ in range(padding):
            row.insert(0, ".")
            row.append(".")

    grid.append(["." for _ in range(padding + row_length + padding)])
    grid.append(["#" for _ in range(padding + row_length + padding)])

    return pour_sand(grid, x_offset)


if __name__ == "__main__":
    day14_input = read_input("input.txt")
    print(part_one(day14_input))
    print(part_two(day14_input))
