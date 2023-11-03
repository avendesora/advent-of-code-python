from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2022.day14.main import draw_grid
from advent_of_code_2022.day14.main import part_one
from advent_of_code_2022.day14.main import part_two
from advent_of_code_2022.day14.main import read_input
from helpers import Point2D

CURRENT_DIRECTORY = Path(Path(os.path.realpath(__file__)).parent)


def test_read_input() -> None:
    input_data, min_x, max_x, max_y = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == [
        [
            Point2D(x=498, y=4),
            Point2D(x=498, y=6),
            Point2D(x=496, y=6),
        ],
        [
            Point2D(x=503, y=4),
            Point2D(x=502, y=4),
            Point2D(x=502, y=9),
            Point2D(x=494, y=9),
        ],
    ]
    assert min_x == 494
    assert max_x == 503
    assert max_y == 9


def test_part_one() -> None:
    input_data, min_x, max_x, max_y = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    grid = draw_grid(input_data, min_x, max_x, max_y)
    assert part_one(grid, min_x) == 24


def test_part_two() -> None:
    input_data, min_x, max_x, max_y = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    grid = draw_grid(input_data, min_x, max_x, max_y)
    assert part_two(grid, min_x) == 93
