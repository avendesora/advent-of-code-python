from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2021.day11.main import count_flashes
from advent_of_code_2021.day11.main import find_first_simultaneous_flash
from advent_of_code_2021.day11.main import take_step
from advent_of_code_2021.day11.main import take_steps
from helpers import read_input_as_2d_int_array

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_day_11_read_input() -> None:
    sample_input = read_input_as_2d_int_array(CURRENT_DIRECTORY / "sample_input.txt")
    assert sample_input == [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]


def test_day_11_part_one() -> None:
    step1 = take_step(
        read_input_as_2d_int_array(CURRENT_DIRECTORY / "sample_input.txt")
    )
    assert step1 == [
        [6, 5, 9, 4, 2, 5, 4, 3, 3, 4],
        [3, 8, 5, 6, 9, 6, 5, 8, 2, 2],
        [6, 3, 7, 5, 6, 6, 7, 2, 8, 4],
        [7, 2, 5, 2, 4, 4, 7, 2, 5, 7],
        [7, 4, 6, 8, 4, 9, 6, 5, 8, 9],
        [5, 2, 7, 8, 6, 3, 5, 7, 5, 6],
        [3, 2, 8, 7, 9, 5, 2, 8, 3, 2],
        [7, 9, 9, 3, 9, 9, 2, 2, 4, 5],
        [5, 9, 5, 7, 9, 5, 9, 6, 6, 5],
        [6, 3, 9, 4, 8, 6, 2, 6, 3, 7],
    ]

    step2 = take_step(step1)
    assert step2 == [
        [8, 8, 0, 7, 4, 7, 6, 5, 5, 5],
        [5, 0, 8, 9, 0, 8, 7, 0, 5, 4],
        [8, 5, 9, 7, 8, 8, 9, 6, 0, 8],
        [8, 4, 8, 5, 7, 6, 9, 6, 0, 0],
        [8, 7, 0, 0, 9, 0, 8, 8, 0, 0],
        [6, 6, 0, 0, 0, 8, 8, 9, 8, 9],
        [6, 8, 0, 0, 0, 0, 5, 9, 4, 3],
        [0, 0, 0, 0, 0, 0, 7, 4, 5, 6],
        [9, 0, 0, 0, 0, 0, 0, 8, 7, 6],
        [8, 7, 0, 0, 0, 0, 6, 8, 4, 8],
    ]
    assert count_flashes(step2) == 35

    step3 = take_step(step2)
    step4 = take_step(step3)
    step5 = take_step(step4)
    step6 = take_step(step5)
    step7 = take_step(step6)
    step8 = take_step(step7)
    step9 = take_step(step8)
    step10 = take_step(step9)

    assert step10 == [
        [0, 4, 8, 1, 1, 1, 2, 9, 7, 6],
        [0, 0, 3, 1, 1, 1, 2, 0, 0, 9],
        [0, 0, 4, 1, 1, 1, 2, 5, 0, 4],
        [0, 0, 8, 1, 1, 1, 1, 4, 0, 6],
        [0, 0, 9, 9, 1, 1, 1, 3, 0, 6],
        [0, 0, 9, 3, 5, 1, 1, 2, 3, 3],
        [0, 4, 4, 2, 3, 6, 1, 1, 3, 0],
        [5, 5, 3, 2, 2, 5, 2, 3, 5, 0],
        [0, 5, 3, 2, 2, 5, 0, 6, 0, 0],
        [0, 0, 3, 2, 2, 4, 0, 0, 0, 0],
    ]

    assert (
        take_steps(
            read_input_as_2d_int_array(CURRENT_DIRECTORY / "sample_input.txt"), 10
        )
        == 204
    )
    assert (
        take_steps(
            read_input_as_2d_int_array(CURRENT_DIRECTORY / "sample_input.txt"), 100
        )
        == 1656
    )


def test_day_11_part_two() -> None:
    sample_input = read_input_as_2d_int_array(CURRENT_DIRECTORY / "sample_input.txt")
    assert find_first_simultaneous_flash(sample_input) == 195
