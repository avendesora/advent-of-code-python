from __future__ import annotations

import logging
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache
from typing import TYPE_CHECKING

from helpers import Point2D
from helpers import read_input_as_string_array
from helpers.logger import get_logger

if TYPE_CHECKING:
    from pathlib import Path

LOGGER = get_logger("2022-day-15", logging.DEBUG)


class NoGoodPointFoundError(Exception):
    ...


@lru_cache
def get_distance(point1: Point2D, point2: Point2D) -> int:
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)


@dataclass
class InputItem:
    sensor_location: Point2D
    closest_beacon_location: Point2D

    @property
    def distance(self: InputItem) -> int:
        return get_distance(self.sensor_location, self.closest_beacon_location)


def read_input(filename: Path | str) -> tuple[list[InputItem], int, int]:
    input_items: list[InputItem] = []
    x_values: list[int] = []

    for line in read_input_as_string_array(filename):
        sensor, beacon = line.split(": ")
        sensor = sensor.replace("Sensor at ", "").replace("x=", "").replace(" y=", "")
        beacon = (
            beacon.replace("closest beacon is at ", "")
            .replace("x=", "")
            .replace(" y=", "")
        )
        sensor_x, sensor_y = (int(value) for value in sensor.split(","))
        beacon_x, beacon_y = (int(value) for value in beacon.split(","))
        input_items.append(
            InputItem(Point2D(sensor_x, sensor_y), Point2D(beacon_x, beacon_y)),
        )
        x_values.extend([sensor_x, beacon_x])

    return input_items, min(x_values), max(x_values)


def part_one(
    input_data: list[InputItem],
    row_to_check: int,
    min_x: int,
    max_x: int,
) -> int:
    differences: list[int] = [input_item.distance for input_item in input_data]
    # offset: int = abs(max_x - min_x)
    offset: int = max(differences)
    no_beacon_x_values: set[int] = set()
    x_indexes_with_sensor_or_beacon: set[int] = set()

    for input_item in input_data:
        if input_item.sensor_location.y == row_to_check:
            x_indexes_with_sensor_or_beacon.add(input_item.sensor_location.x)

        if input_item.closest_beacon_location.y == row_to_check:
            x_indexes_with_sensor_or_beacon.add(input_item.closest_beacon_location.x)

    for x_index in range(min_x - offset, max_x + offset + 1):
        current_point: Point2D = Point2D(x_index, row_to_check)
        LOGGER.debug("loop 2: %d", x_index)

        for input_item in input_data:
            if (
                input_item.closest_beacon_location.y == row_to_check
                and input_item.closest_beacon_location.x == x_index
            ):
                no_beacon_x_values.add(x_index)
                break

            if (
                input_item.sensor_location.y == row_to_check
                and input_item.sensor_location.x == x_index
            ):
                no_beacon_x_values.add(x_index)
                break

            distance_from_sensor = get_distance(
                input_item.sensor_location,
                current_point,
            )

            if distance_from_sensor <= input_item.distance:
                no_beacon_x_values.add(x_index)
                break

    # debug_list = list(no_beacon_x_values)
    # debug_list.sort()

    return len(no_beacon_x_values - x_indexes_with_sensor_or_beacon)


def part_two(input_data: list[InputItem], min_value: int, max_value: int) -> int | None:
    # TODO - since there is only one beacon, it has to be distance + 1 away from at
    # TODO - least one of the sensors, so, find all of the points that are distance + 1
    # TODO - away from each sensor and with the defined range and then check each of
    # TODO - those points to see if they are valid, return for the first valid point
    # TODO - found.

    beacon_point = None
    occupied_points: set[Point2D] = set()

    for input_item in input_data:
        occupied_points.add(input_item.sensor_location)
        occupied_points.add(input_item.closest_beacon_location)

    for y in range(min_value, max_value):
        LOGGER.debug(y)
        ranges: dict[int, int] = defaultdict(int)

        for input_item in input_data:
            sensor = input_item.sensor_location
            highest = input_item.distance - get_distance(sensor, Point2D(sensor.x, y))

            if highest < 0:
                continue

            left = max(0, sensor.x - highest)
            right = min(max_value, sensor.x + highest)
            ranges[left] += 1
            ranges[right + 1] -= 1
            cur = 0

        for key in sorted(ranges.keys()):
            cur += ranges[key]

            if cur == 0 and key != max_value + 1:
                beacon_point = Point2D(key, y)
                break

    if beacon_point is None:
        error_message = "no good point found for beacon"
        raise NoGoodPointFoundError(error_message)

    return beacon_point.x * 4000000 + beacon_point.y


if __name__ == "__main__":
    day15_input, x_min, x_max = read_input("input.txt")
    LOGGER.info(part_one(day15_input, 2000000, x_min, x_max))
    LOGGER.info(part_two(day15_input, 0, 4000000))
