from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2022.day11.main import Monkey
from advent_of_code_2022.day11.main import part_one
from advent_of_code_2022.day11.main import part_two
from advent_of_code_2022.day11.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == {
        0: Monkey(
            monkey_id=0,
            starting_items=[79, 98],
            operation="*",
            operand="19",
            test_divisor=23,
            if_true=2,
            if_false=3,
        ),
        1: Monkey(
            monkey_id=1,
            starting_items=[54, 65, 75, 74],
            operation="+",
            operand="6",
            test_divisor=19,
            if_true=2,
            if_false=0,
        ),
        2: Monkey(
            monkey_id=2,
            starting_items=[79, 60, 97],
            operation="*",
            operand="old",
            test_divisor=13,
            if_true=1,
            if_false=3,
        ),
        3: Monkey(
            monkey_id=3,
            starting_items=[74],
            operation="+",
            operand="3",
            test_divisor=17,
            if_true=0,
            if_false=1,
        ),
    }


def test_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_one(input_data) == 10605


def test_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_two(input_data) == 2713310158
