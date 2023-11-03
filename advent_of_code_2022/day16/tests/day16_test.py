from __future__ import annotations

import os
from pathlib import Path

import pytest

from advent_of_code_2022.day16.main import Valve
from advent_of_code_2022.day16.main import part_one
from advent_of_code_2022.day16.main import part_two
from advent_of_code_2022.day16.main import read_input

CURRENT_DIRECTORY = Path(Path(os.path.realpath(__file__)).parent)


def test_read_input() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert input_data == [
        Valve(name="AA", flow_rate=0, tunnels=["DD", "II", "BB"]),
        Valve(name="BB", flow_rate=13, tunnels=["CC", "AA"]),
        Valve(name="CC", flow_rate=2, tunnels=["DD", "BB"]),
        Valve(name="DD", flow_rate=20, tunnels=["CC", "AA", "EE"]),
        Valve(name="EE", flow_rate=3, tunnels=["FF", "DD"]),
        Valve(name="FF", flow_rate=0, tunnels=["EE", "GG"]),
        Valve(name="GG", flow_rate=0, tunnels=["FF", "HH"]),
        Valve(name="HH", flow_rate=22, tunnels=["GG"]),
        Valve(name="II", flow_rate=0, tunnels=["AA", "JJ"]),
        Valve(name="JJ", flow_rate=21, tunnels=["II"]),
    ]


@pytest.mark.xfail()
def test_part_one() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_one(input_data) == 1651


@pytest.mark.xfail()
def test_part_two() -> None:
    input_data = read_input(CURRENT_DIRECTORY / "sample_input.txt")
    assert part_two(input_data) is not None
