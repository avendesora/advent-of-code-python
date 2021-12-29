from day10.main import (
    check_line,
    get_invalid_characters,
    get_syntax_error_score,
    get_completion_string,
    get_completion_string_score,
    get_final_completion_score,
)
from helpers import read_input_as_string_array


def test_day_10_read_input():
    sample_input = read_input_as_string_array("sample_input.txt")
    assert sample_input == [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]


def test_day_10_part_one():
    sample_input = read_input_as_string_array("sample_input.txt")

    assert check_line(sample_input[0]) == (
        True,
        ["[", "(", "{", "(", "[", "[", "{", "{"],
    )
    assert check_line(sample_input[1]) == (True, ["(", "{", "[", "<", "{", "("])
    assert check_line(sample_input[2]) == (False, ["}"])
    assert check_line(sample_input[3]) == (
        True,
        ["(", "(", "(", "(", "<", "{", "<", "{", "{"],
    )
    assert check_line(sample_input[4]) == (False, [")"])
    assert check_line(sample_input[5]) == (False, ["]"])
    assert check_line(sample_input[6]) == (
        True,
        ["<", "{", "[", "{", "[", "{", "{", "[", "["],
    )
    assert check_line(sample_input[7]) == (False, [")"])
    assert check_line(sample_input[8]) == (False, [">"])
    assert check_line(sample_input[9]) == (True, ["<", "{", "(", "["])

    assert get_invalid_characters(sample_input) == ["}", ")", "]", ")", ">"]

    assert get_syntax_error_score(sample_input) == 26397


def test_day_10_part_two():
    sample_input = read_input_as_string_array("sample_input.txt")

    _, stack0 = check_line(sample_input[0])
    _, stack1 = check_line(sample_input[1])
    _, stack3 = check_line(sample_input[3])
    _, stack6 = check_line(sample_input[6])
    _, stack9 = check_line(sample_input[9])

    completion_string0 = get_completion_string(stack0)
    completion_string1 = get_completion_string(stack1)
    completion_string3 = get_completion_string(stack3)
    completion_string6 = get_completion_string(stack6)
    completion_string9 = get_completion_string(stack9)

    assert completion_string0 == "}}]])})]"
    assert completion_string1 == ")}>]})"
    assert completion_string3 == "}}>}>))))"
    assert completion_string6 == "]]}}]}]}>"
    assert completion_string9 == "])}>"

    score0 = get_completion_string_score(completion_string0)
    score1 = get_completion_string_score(completion_string1)
    score3 = get_completion_string_score(completion_string3)
    score6 = get_completion_string_score(completion_string6)
    score9 = get_completion_string_score(completion_string9)

    assert score0 == 288957
    assert score1 == 5566
    assert score3 == 1480781
    assert score6 == 995444
    assert score9 == 294

    assert get_final_completion_score(sample_input) == 288957
