from typing import Union

OPEN_AND_CLOSE_CHARACTERS: dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

ERROR_SCORES: dict[str, int] = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

COMPLETION_SCORES: dict[str, int] = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def read_input(filename: str) -> list[str]:
    input_lines: list[str] = []

    with open(filename, "r", encoding="utf-8") as file_lines:
        for file_line in file_lines:
            input_lines.append(_clean_line(file_line))

    return input_lines


def _clean_line(file_line: str) -> str:
    return file_line.replace("\n", "")


def check_line(input_line: str) -> tuple[bool, list[str]]:
    stack: list[str] = []

    for character in input_line:
        if not stack and character not in OPEN_AND_CLOSE_CHARACTERS.keys():
            return False, [character]

        if character in OPEN_AND_CLOSE_CHARACTERS.keys():
            stack.append(character)
            continue

        previous_character = stack.pop()

        if character != OPEN_AND_CLOSE_CHARACTERS.get(previous_character):
            return False, [character]

    return True, stack


def get_invalid_characters(input_lines: list[str]) -> list[str]:
    invalid_characters: list[str] = []

    for input_line in input_lines:
        is_valid, invalid_character = check_line(input_line)

        if not is_valid:
            invalid_characters.extend(invalid_character)

    return invalid_characters


def get_syntax_error_score(input_lines: list[str]) -> int:
    return sum(
        ERROR_SCORES.get(invalid_character, 0)
        for invalid_character in get_invalid_characters(input_lines)
    )


def get_completion_string(stack: list[str]) -> str:
    return "".join(
        OPEN_AND_CLOSE_CHARACTERS.get(character, "")
        for character in reversed(stack)
    )


def get_completion_string_score(completion_string: str) -> int:
    completion_string_score = 0

    for character in completion_string:
        completion_string_score *= 5
        completion_string_score += COMPLETION_SCORES.get(character, 0)

    return completion_string_score


def get_final_completion_score(input_lines: list[str]) -> int:
    completion_scores: list[int] = []

    for input_line in input_lines:
        is_valid, characters = check_line(input_line)

        if not is_valid:
            continue

        completion_string = get_completion_string(characters)
        completion_scores.append(get_completion_string_score(completion_string))

    completion_scores.sort()

    return completion_scores[len(completion_scores) // 2]


if __name__ == "__main__":
    lines = read_input("input.txt")

    # Part One
    print(f"The total syntax error score is {get_syntax_error_score(lines)}.")

    # Part Two
    print(f"The completion score is {get_final_completion_score(lines)}.")
