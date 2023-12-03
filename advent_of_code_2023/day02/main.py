from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from helpers import read_input_as_string_array
from helpers.logger import get_logger

if TYPE_CHECKING:
    from pathlib import Path


LOGGER = get_logger("2023-day-02")


@dataclass
class GameRound:
    red_count: int
    blue_count: int
    green_count: int


@dataclass
class Game:
    game_id: int
    game_rounds: list[GameRound]
    possible: bool
    red_minimum: int
    green_minimum: int
    blue_minimum: int


def create_game_round(game_round_string: str) -> GameRound:
    red_count = 0
    green_count = 0
    blue_count = 0
    cube_strings = game_round_string.split(", ")

    for cube_string in cube_strings:
        cube_count, cube_color = cube_string.split(" ")

        if cube_color == "red":
            red_count = int(cube_count)

        elif cube_color == "green":
            green_count = int(cube_count)

        elif cube_color == "blue":
            blue_count = int(cube_count)

    return GameRound(
        red_count=red_count,
        green_count=green_count,
        blue_count=blue_count,
    )


def create_game(line: str) -> Game:
    game_string, game_rounds_string = line.split(": ")
    _, game_id = game_string.split(" ")

    game_rounds = [
        create_game_round(game_round) for game_round in game_rounds_string.split("; ")
    ]

    red_minimum = max(game_round.red_count for game_round in game_rounds)
    green_minimum = max(game_round.green_count for game_round in game_rounds)
    blue_minimum = max(game_round.blue_count for game_round in game_rounds)

    is_possible = red_minimum <= 12 and green_minimum <= 13 and blue_minimum <= 14

    return Game(
        game_id=int(game_id),
        game_rounds=game_rounds,
        possible=is_possible,
        red_minimum=red_minimum,
        green_minimum=green_minimum,
        blue_minimum=blue_minimum,
    )


def read_input(filename: Path | str) -> list[Game]:
    return [create_game(line) for line in read_input_as_string_array(filename)]


def part_one(games: list[Game]) -> int:
    return sum(game.game_id for game in games if game.possible)


def part_two(games: list[Game]) -> int:
    return sum(
        game.red_minimum * game.green_minimum * game.blue_minimum for game in games
    )


if __name__ == "__main__":
    input_data = read_input("input.txt")
    part_one_result = part_one(input_data)
    LOGGER.info("part one = %d", part_one_result)
    part_two_result = part_two(input_data)
    LOGGER.info("part two = %d", part_two_result)
