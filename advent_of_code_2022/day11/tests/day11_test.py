import os
from pathlib import Path

from advent_of_code_2022.day11.main import Monkey
from advent_of_code_2022.day11.main import Test
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
            operation="new = old * 19",
            test=Test(
                test="divisible by 23",
                if_true="throw to monkey 2",
                if_false="throw to monkey 3",
            ),
        ),
        1: Monkey(
            monkey_id=1,
            starting_items=[54, 65, 75, 74],
            operation="new = old + 6",
            test=Test(
                test="divisible by 19",
                if_true="throw to monkey 2",
                if_false="throw to monkey 0",
            ),
        ),
        2: Monkey(
            monkey_id=2,
            starting_items=[79, 60, 97],
            operation="new = old * old",
            test=Test(
                test="divisible by 13",
                if_true="throw to monkey 1",
                if_false="throw to monkey 3",
            ),
        ),
        3: Monkey(
            monkey_id=3,
            starting_items=[74],
            operation="new = old + 3",
            test=Test(
                test="divisible by 17",
                if_true="throw to monkey 0",
                if_false="throw to monkey 1",
            ),
        ),
    }


def test_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_one(input_data) == 10605


def test_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_two(input_data) is not None
