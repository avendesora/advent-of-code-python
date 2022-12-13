from __future__ import annotations

import os
from pathlib import Path

from advent_of_code_2021.day15.main import get_edges
from advent_of_code_2021.day15.main import get_full_risk_levels
from advent_of_code_2021.day15.main import increase_risk
from helpers import read_input_as_2d_int_array
from helpers.simple_dijkstra import get_weighted_graph

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))


def test_day_15_read_input(input_array: list[list[int]]) -> None:
    risk_levels = read_input_as_2d_int_array(CURRENT_DIRECTORY / "sample_input.txt")

    assert risk_levels == input_array


def test_get_edges(
    input_array: list[list[int]],
    edges: list[tuple[int, int, int]],
) -> None:
    input_edges = get_edges(input_array)

    assert input_edges == edges


def test_get_total_least_risk(edges: list[tuple[int, int, int]]) -> None:
    graph = get_weighted_graph(edges, 100)
    lowest_total_risk = graph.get_total_least_weight()

    assert lowest_total_risk == 40


def test_increase_risk(
    input_array: list[list[int]],
    input_array_increased_once: list[list[int]],
    input_array_increased_twice: list[list[int]],
) -> None:
    risk_levels_increased_once = increase_risk(input_array)

    assert risk_levels_increased_once == input_array_increased_once

    risk_levels_increased_twice = increase_risk(risk_levels_increased_once)

    assert risk_levels_increased_twice == input_array_increased_twice


def test_get_full_risk_levels() -> None:
    risk_levels = read_input_as_2d_int_array(CURRENT_DIRECTORY / "sample_input.txt")
    expected_full_risk_levels = read_input_as_2d_int_array(
        CURRENT_DIRECTORY / "full_sample_input.txt"
    )

    actual_full_risk_levels = get_full_risk_levels(risk_levels)

    assert actual_full_risk_levels == expected_full_risk_levels


def test_get_total_least_risk_full_risk_levels() -> None:
    risk_levels = read_input_as_2d_int_array(CURRENT_DIRECTORY / "sample_input.txt")
    full_risk_levels = get_full_risk_levels(risk_levels)
    edges = get_edges(full_risk_levels)
    graph = get_weighted_graph(edges, 100 * 25)
    lowest_total_risk = graph.get_total_least_weight()

    assert lowest_total_risk == 315
