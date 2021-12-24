from day09.main import read_input, get_risk_level, get_basins, get_product_size


def test_day_09_read_input():
    sample_input = read_input("sample_input.txt")
    assert sample_input == [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]


def test_day_09_part_one():
    sample_input = read_input("sample_input.txt")
    assert get_risk_level(sample_input) == 15


def test_day_09_part_two():
    sample_input = read_input("sample_input.txt")
    basins: list[set[str]] = get_basins(sample_input)
    assert get_product_size(basins, 3) == 1134
