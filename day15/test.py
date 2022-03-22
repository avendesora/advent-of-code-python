from day15.main import get_risk_graph, get_total_least_risk, read_input


def test_day_15_read_input(edges, vertices):
    input_edges, input_vertices = read_input("sample_input.txt")

    assert input_edges == edges
    assert input_vertices == vertices


def test_get_total_least_risk(edges, vertices):
    graph = get_risk_graph(edges, vertices)
    lowest_total_risk = get_total_least_risk(graph, vertices)

    assert lowest_total_risk == 40
