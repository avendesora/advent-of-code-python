from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2022.day15.main import InputItem
from advent_of_code_2022.day15.main import part_one
from advent_of_code_2022.day15.main import part_two
from advent_of_code_2022.day15.main import read_input
from helpers import Point2D

CURRENT_DIRECTORY = Path(Path(os.path.realpath(__file__)).parent)


def test_read_input() -> None:
    input_data, min_x, max_x = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == [
        InputItem(
            sensor_location=Point2D(x=2, y=18),
            closest_beacon_location=Point2D(x=-2, y=15),
        ),
        InputItem(
            sensor_location=Point2D(x=9, y=16),
            closest_beacon_location=Point2D(x=10, y=16),
        ),
        InputItem(
            sensor_location=Point2D(x=13, y=2),
            closest_beacon_location=Point2D(x=15, y=3),
        ),
        InputItem(
            sensor_location=Point2D(x=12, y=14),
            closest_beacon_location=Point2D(x=10, y=16),
        ),
        InputItem(
            sensor_location=Point2D(x=10, y=20),
            closest_beacon_location=Point2D(x=10, y=16),
        ),
        InputItem(
            sensor_location=Point2D(x=14, y=17),
            closest_beacon_location=Point2D(x=10, y=16),
        ),
        InputItem(
            sensor_location=Point2D(x=8, y=7),
            closest_beacon_location=Point2D(x=2, y=10),
        ),
        InputItem(
            sensor_location=Point2D(x=2, y=0),
            closest_beacon_location=Point2D(x=2, y=10),
        ),
        InputItem(
            sensor_location=Point2D(x=0, y=11),
            closest_beacon_location=Point2D(x=2, y=10),
        ),
        InputItem(
            sensor_location=Point2D(x=20, y=14),
            closest_beacon_location=Point2D(x=25, y=17),
        ),
        InputItem(
            sensor_location=Point2D(x=17, y=20),
            closest_beacon_location=Point2D(x=21, y=22),
        ),
        InputItem(
            sensor_location=Point2D(x=16, y=7),
            closest_beacon_location=Point2D(x=15, y=3),
        ),
        InputItem(
            sensor_location=Point2D(x=14, y=3),
            closest_beacon_location=Point2D(x=15, y=3),
        ),
        InputItem(
            sensor_location=Point2D(x=20, y=1),
            closest_beacon_location=Point2D(x=15, y=3),
        ),
    ]
    assert min_x == -2
    assert max_x == 25


def test_part_one() -> None:
    input_data, min_x, max_x = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_one(input_data, 10, min_x, max_x) == 26


def test_part_two() -> None:
    input_data, min_x, max_x = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_two(input_data, 0, 20) == 56000011
