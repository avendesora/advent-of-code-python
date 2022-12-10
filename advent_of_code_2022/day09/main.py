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
        return -1 if self == Direction.LEFT else 1 if self == Direction.RIGHT else 0

    @property
    def y_value(self: Direction) -> int:
        return 1 if self == Direction.UP else -1 if self == Direction.DOWN else 0


@dataclass(eq=True, frozen=True)
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

    if x_diff > 0:  # Need to move left or right
        if previous_knot.x > current_knot.x:  # Right
            new_x += 1
        else:  # Left
            new_x -= 1

    if y_diff > 0:  # Need to move up or down
        if previous_knot.y > current_knot.y:  # Up
            new_y += 1
        else:  # Down
            new_y -= 1

    return Point2D(new_x, new_y)


def get_tail_locations(
    input_data: list[Motion], number_of_knots: int = 2
) -> set[Point2D]:
    starting_point = Point2D(0, 0)
    knots: list[Point2D] = [starting_point for _ in range(number_of_knots)]
    tail_locations: set[Point2D] = {starting_point}

    # Go through the specified motions
    for motion in input_data:
        # Move the specified number of steps in the specified direction
        for _ in range(motion.number_of_steps):
            # Update each knot from the head to the tail
            for index, knot in enumerate(knots):
                if index == 0:  # Head
                    knot = Point2D(
                        knot.x + motion.direction.x_value,
                        knot.y + motion.direction.y_value,
                    )
                else:  # All other knots
                    knot = move_next_knot(knots[index - 1], knot)

                knots[index] = knot

            # Add the tail knot location (the last knot) to the set of tail locations.
            tail_locations.add(knots[-1])

    return tail_locations


def part_one(input_data: list[Motion]) -> int:
    return len(get_tail_locations(input_data))


def part_two(input_data: list[Motion]) -> int:
    return len(get_tail_locations(input_data, 10))


if __name__ == "__main__":
    day9_input = read_input("input.txt")
    print(part_one(day9_input))
    print(part_two(day9_input))
