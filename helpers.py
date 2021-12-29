def read_input_as_int_array(filename: str) -> list[int]:
    with open(filename, "r", encoding="utf-8") as lines:
        return [int(clean_line(line)) for line in lines if clean_line(line).isnumeric()]


def read_input_as_int_array_from_csv(filename: str) -> list[int]:
    with open(filename, "r", encoding="utf-8") as file_lines:
        return [int(x) for x in file_lines.readline().split(",")]


def read_input_as_2d_int_array(filename: str) -> list[list[int]]:
    input_2d_array: list[list[int]] = []

    with open(filename, "r", encoding="utf-8") as file_lines:
        for file_line in file_lines:
            clean_file_line = clean_line(file_line).strip()

            if len(clean_file_line) == 0:
                continue

            input_2d_array.append([int(character) for character in clean_file_line])

    return input_2d_array


def read_input_as_string_array(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as lines:
        return [clean_line(line) for line in lines if clean_line(line)]


def clean_line(file_line: str) -> str:
    return file_line.replace("\n", "")


def transpose_2d_int_array(input_array: list[list[int]]) -> list[list[int]]:
    return [list(x) for x in zip(*input_array)]
