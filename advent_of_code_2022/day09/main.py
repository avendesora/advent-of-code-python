from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from helpers import Point2D
from helpers import read_input_as_string_array


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"
    UP = "U"
    DOWN = "D"

    @property
    def x_value(self: Direction) -> int:
        return DIRECTION_X_Y_VALUES[self][0]

    @property
    def y_value(self: Direction) -> int:
        return DIRECTION_X_Y_VALUES[self][1]


DIRECTION_X_Y_VALUES: dict[Direction, tuple[int, int]] = {
    Direction.LEFT: (-1, 0),
    Direction.RIGHT: (1, 0),
    Direction.UP: (0, 1),
    Direction.DOWN: (0, -1),
}


@dataclass
class Motion:
    direction: Direction
    number_of_steps: int


def read_input(filename: Path | str) -> list[Motion]:
    lines = read_input_as_string_array(filename)
    motions: list[Motion] = []

    for line in lines:
        direction, number_of_steps = line.split()
        motions.append(Motion(Direction(direction), int(number_of_steps)))

    return motions


def move_next_knot(previous_knot: Point2D, current_knot: Point2D) -> Point2D:
    x_diff = abs(current_knot.x - previous_knot.x)
    y_diff = abs(current_knot.y - previous_knot.y)

    # no need to move
    if x_diff <= 1 and y_diff <= 1:
        return current_knot

    new_x = current_knot.x
    new_y = current_knot.y

    if x_diff > 0:
        if previous_knot.x > current_knot.x:
            new_x += 1
        else:
            new_x -= 1

    if y_diff > 0:
        if previous_knot.y > current_knot.y:
            new_y += 1
        else:
            new_y -= 1

    return Point2D(new_x, new_y)


def get_tail_locations(
    input_data: list[Motion], number_of_knots: int = 2
) -> list[Point2D]:
    starting_point = Point2D(0, 0)
    knots: list[Point2D] = [starting_point for _ in range(number_of_knots)]
    tail_locations: list[Point2D] = [starting_point]

    for motion in input_data:
        for _ in range(motion.number_of_steps):
            for index, knot in enumerate(knots):
                if index == 0:
                    knot = Point2D(
                        knot.x + motion.direction.x_value,
                        knot.y + motion.direction.y_value,
                    )
                else:
                    knot = move_next_knot(knots[index - 1], knot)

                knots[index] = knot

            if knots[-1] not in tail_locations:
                tail_locations.append(knots[-1])

    return tail_locations


def part_one(input_data: list[Motion]) -> int:
    tail_locations = get_tail_locations(input_data)
    return len(tail_locations)


def part_two(input_data: list[Motion]) -> int:
    tail_locations = get_tail_locations(input_data, 10)
    return len(tail_locations)


if __name__ == "__main__":
    day9_input = read_input("input.txt")
    print(part_one(day9_input))
    print(part_two(day9_input))
