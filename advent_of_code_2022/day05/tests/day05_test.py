from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2022.day05.main import Instruction
from advent_of_code_2022.day05.main import part_one
from advent_of_code_2022.day05.main import part_two
from advent_of_code_2022.day05.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input() -> None:
    stacks, instructions = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert stacks == [
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"],
    ]
    assert instructions == [
        Instruction(count=1, from_stack=2, to_stack=1),
        Instruction(count=3, from_stack=1, to_stack=3),
        Instruction(count=2, from_stack=2, to_stack=1),
        Instruction(count=1, from_stack=1, to_stack=2),
    ]


def test_day_05_part_one() -> None:
    stacks, instructions = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_one(stacks, instructions) == "CMZ"


def test_day_05_part_two() -> None:
    stacks, instructions = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_two(stacks, instructions) == "MCD"
