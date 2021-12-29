from day12.main import find_valid_paths, make_graph, read_input


def test_day_12_read_input(sample_data1):
    sample_input = read_input("sample_input.txt")
    assert sample_input == sample_data1


def test_day_12_part_one(
    sample_data1, sample_data2, sample_data3, valid_paths1, valid_paths2
):
    paths1 = find_valid_paths(make_graph(sample_data1))
    path_strings1 = {", ".join(path) for path in paths1}
    assert path_strings1 == valid_paths1

    paths2 = find_valid_paths(make_graph(sample_data2))
    path_strings2 = {", ".join(path) for path in paths2}
    assert path_strings2 == valid_paths2

    paths3 = find_valid_paths(make_graph(sample_data3))
    assert len(paths3) == 226


def test_day_12_part_two(sample_data1, sample_data2, sample_data3, valid_paths1b):
    paths1 = find_valid_paths(make_graph(sample_data1), 2)
    path_strings1 = {", ".join(path) for path in paths1}
    assert path_strings1 == valid_paths1b

    paths2 = find_valid_paths(make_graph(sample_data2), 2)
    assert len(paths2) == 103

    paths3 = find_valid_paths(make_graph(sample_data3), 2)
    assert len(paths3) == 3509
