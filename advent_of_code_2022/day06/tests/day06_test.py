from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2022.day06.main import part_one
from advent_of_code_2022.day06.main import part_two
from advent_of_code_2022.day06.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_day_06_part_one() -> None:
    assert part_one("abcd") == 4
    assert part_one("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert part_one("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert part_one("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert part_one("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert part_one("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_day_06_part_two() -> None:
    assert part_two("abcdefghijklmn") == 14
    assert part_two("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert part_two("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert part_two("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert part_two("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert part_two("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
