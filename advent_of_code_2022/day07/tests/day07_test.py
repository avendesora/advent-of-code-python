from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2022.day07.main import generate_directory_structure
from advent_of_code_2022.day07.main import get_sizes
from advent_of_code_2022.day07.main import part_one
from advent_of_code_2022.day07.main import part_two
from advent_of_code_2022.day07.main import read_input

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]


def test_day_07_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    root = generate_directory_structure(input_data)
    sizes = get_sizes(root)
    assert part_one(sizes) == 95437


def test_day_07_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    root = generate_directory_structure(input_data)
    sizes = get_sizes(root)
    assert part_two(root, sizes) == 24933642
