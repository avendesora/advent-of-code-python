from helpers import read_input_as_2d_int_array

from day15.main import get_edges, get_full_risk_levels, get_risk_graph, increase_risk


def test_day_15_read_input(input_array):
    risk_levels = read_input_as_2d_int_array("sample_input.txt")

    assert risk_levels == input_array


def test_get_edges(input_array, edges):
    input_edges = get_edges(input_array)

    assert input_edges == edges


def test_get_total_least_risk(edges):
    graph = get_risk_graph(edges, 100)
    lowest_total_risk = graph.get_total_least_risk()

    assert lowest_total_risk == 40


def test_increase_risk(
    input_array, input_array_increased_once, input_array_increased_twice
):
    risk_levels_increased_once = increase_risk(input_array)

    assert risk_levels_increased_once == input_array_increased_once

    risk_levels_increased_twice = increase_risk(risk_levels_increased_once)

    assert risk_levels_increased_twice == input_array_increased_twice


def test_get_full_risk_levels():
    risk_levels = read_input_as_2d_int_array("sample_input.txt")
    expected_full_risk_levels = read_input_as_2d_int_array("full_sample_input.txt")
    actual_full_risk_levels = get_full_risk_levels(risk_levels)

    assert actual_full_risk_levels == expected_full_risk_levels


def test_get_total_least_risk_full_risk_levels():
    risk_levels = read_input_as_2d_int_array("sample_input.txt")
    full_risk_levels = get_full_risk_levels(risk_levels)
    edges = get_edges(full_risk_levels)
    graph = get_risk_graph(edges, 100 * 25)
    lowest_total_risk = graph.get_total_least_risk()

    assert lowest_total_risk == 315
