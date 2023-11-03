from __future__ import annotations

from enum import IntEnum
from pathlib import Path

from helpers import clean_line
from helpers.logger import get_logger

LOGGER = get_logger("2022-day-02")

WIN_SCORE = 6
LOSS_SCORE = 0
TIE_SCORE = 3


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @staticmethod
    def get_shape(character: str) -> Shape:
        return (
            Shape.ROCK
            if character in {"A", "X"}
            else Shape.PAPER
            if character in {"B", "Y"}
            else Shape.SCISSORS
        )


def read_input(filename: Path | str) -> list[list[str]]:
    input_2d_array: list[list[str]] = []

    with Path(filename).open(encoding="utf-8") as file_lines:
        for file_line in file_lines:
            clean_file_line = clean_line(file_line).strip()

            if len(clean_file_line) == 0:
                continue

            input_2d_array.append(clean_file_line.split())

    return input_2d_array


def get_outcome_score(shape1: Shape, shape2: Shape) -> int:
    if shape1 == shape2:
        return TIE_SCORE

    if (
        (shape1 == Shape.ROCK and shape2 == Shape.PAPER)
        or (shape1 == Shape.PAPER and shape2 == Shape.SCISSORS)
        or (shape1 == Shape.SCISSORS and shape2 == Shape.ROCK)
    ):
        return WIN_SCORE

    return LOSS_SCORE


def get_new_shape(shape: Shape, guide: str) -> Shape:
    if guide == "Y":
        return shape

    if guide == "X":
        return (
            Shape.SCISSORS
            if shape == Shape.ROCK
            else Shape.ROCK
            if shape == Shape.PAPER
            else Shape.PAPER
        )

    return (
        Shape.PAPER
        if shape == Shape.ROCK
        else Shape.SCISSORS
        if shape == Shape.PAPER
        else Shape.ROCK
    )


def part_one(input_data: list[list[str]]) -> int:
    total_score = 0

    for game in input_data:
        shape1 = Shape.get_shape(game[0])
        shape2 = Shape.get_shape(game[1])
        outcome_score = get_outcome_score(shape1, shape2)
        game_score = shape2.value + outcome_score
        total_score += game_score

    return total_score


def part_two(input_data: list[list[str]]) -> int:
    total_score = 0

    for game in input_data:
        shape1 = Shape.get_shape(game[0])
        shape2 = get_new_shape(shape1, game[1])
        outcome_score = get_outcome_score(shape1, shape2)
        game_score = shape2.value + outcome_score
        total_score += game_score

    return total_score


if __name__ == "__main__":
    day2_input = read_input("input.txt")
    LOGGER.info(part_one(day2_input))
    LOGGER.info(part_two(day2_input))
