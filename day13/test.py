from day13.main import count_visible_dots, execute_instruction, initialize_pattern, printable_pattern, read_input


def test_day_13_read_input(sample_data):
    assert read_input("sample_input.txt") == sample_data


def test_initialize_pattern(sample_data, initial_pattern):
    dots, _ = sample_data
    pattern = initialize_pattern(dots)

    assert pattern == initial_pattern


def test_printable_pattern(sample_data, pattern_string):
    dots, _ = sample_data
    pattern = initialize_pattern(dots)
    actual_pattern_string = printable_pattern(pattern)

    assert actual_pattern_string == pattern_string


def test_fold_y(sample_data, folded_pattern_y, folded_pattern_y_string):
    dots, instructions = sample_data
    pattern = initialize_pattern(dots)
    actual_folded_pattern = execute_instruction(pattern, instructions[0])
    actual_folded_pattern_string = printable_pattern(actual_folded_pattern)

    assert actual_folded_pattern == folded_pattern_y
    assert actual_folded_pattern_string == folded_pattern_y_string


def test_fold_x(sample_data, folded_pattern_x, folded_pattern_x_string):
    dots, instructions = sample_data
    pattern = initialize_pattern(dots)
    folded_pattern_y = execute_instruction(pattern, instructions[0])
    actual_folded_pattern_x = execute_instruction(folded_pattern_y, instructions[1])
    actual_folded_pattern_x_string = printable_pattern(actual_folded_pattern_x)

    assert actual_folded_pattern_x == folded_pattern_x
    assert actual_folded_pattern_x_string == folded_pattern_x_string


def test_count_dots(sample_data):
    dots, instructions = sample_data
    pattern = initialize_pattern(dots)
    folded_pattern_y = execute_instruction(pattern, instructions[0])

    assert count_visible_dots(folded_pattern_y) == 17

    folded_pattern_x = execute_instruction(folded_pattern_y, instructions[1])

    assert count_visible_dots(folded_pattern_x) == 16
