from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from helpers import read_input_as_string_array
from helpers.logger import get_logger

if TYPE_CHECKING:
    from pathlib import Path

LOGGER = get_logger("2021-day-17", logging.DEBUG)


def read_input(filename: Path | str) -> tuple[tuple[int, int], tuple[int, int]]:
    line = read_input_as_string_array(filename)[0]
    line = line.replace("target area: ", "").replace("x=", "").replace("y=", "")
    x_values, y_values = line.split(", ")
    x_min, x_max = x_values.split("..")
    y_min, y_max = y_values.split("..")

    return (int(x_min), int(x_max)), (int(y_min), int(y_max))


def part_one(min_x: int, max_x: int, min_y: int, max_y: int) -> tuple[int, int]:
    x_current = 0
    y_current = 0

    while x_current < max_x and y_current > max_y:
        ...

        x_current += 1
        y_current -= 1

    LOGGER.debug(min_x)
    LOGGER.debug(min_y)
    return 0, 0


def part_two(input_data: tuple[tuple[int, int], tuple[int, int]]) -> int | None:
    LOGGER.debug(input_data)
    return None


if __name__ == "__main__":
    day17_input = read_input("input.txt")
    part1_result = part_one(
        day17_input[0][0],
        day17_input[0][1],
        day17_input[1][0],
        day17_input[1][1],
    )
    LOGGER.info(part1_result)

    part2_result = part_two(day17_input)
    LOGGER.info(part2_result)
