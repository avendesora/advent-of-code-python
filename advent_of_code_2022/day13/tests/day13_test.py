import os
from pathlib import Path

from advent_of_code_2022.day13.main import PacketPair
from advent_of_code_2022.day13.main import part_one
from advent_of_code_2022.day13.main import part_two
from advent_of_code_2022.day13.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == [
        PacketPair(left=[1, 1, 3, 1, 1], right=[1, 1, 5, 1, 1]),
        PacketPair(left=[[1], [2, 3, 4]], right=[[1], 4]),
        PacketPair(left=[9], right=[[8, 7, 6]]),
        PacketPair(left=[[4, 4], 4, 4], right=[[4, 4], 4, 4, 4]),
        PacketPair(left=[7, 7, 7, 7], right=[7, 7, 7]),
        PacketPair(left=[], right=[3]),
        PacketPair(left=[[[]]], right=[[]]),
        PacketPair(
            left=[1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            right=[1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
        ),
    ]


def test_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_one(input_data) == 13


def test_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    # input_data = [
    #     PacketPair(left=[], right=[[]])
    # ]
    assert part_two(input_data) == 140
