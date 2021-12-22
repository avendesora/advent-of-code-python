def read_input(filename: str) -> list[list[int]]:
    input_2d_array: list[list[int]] = []

    with open(filename, "r", encoding="utf-8") as file_lines:
        for file_line in file_lines:
            clean_file_line = _clean_line(file_line).strip()

            if len(clean_file_line) == 0:
                continue

            input_2d_array.append([int(character) for character in clean_file_line])

    return input_2d_array


def _clean_line(file_line: str) -> str:
    return file_line.replace("\n", "")


if __name__ == "__main__":
    heightmap: list[list[int]] = read_input("input.txt")
    total_risk_level: int = 0

    for row_index, row in enumerate(heightmap):
        for column_index, cell in enumerate(row):
            # Check above
            if row_index > 0:
                if heightmap[row_index - 1][column_index] <= cell:
                    continue

            # Check below
            if row_index < len(heightmap) - 1:
                if heightmap[row_index + 1][column_index] <= cell:
                    continue

            # Check left
            if column_index > 0:
                if heightmap[row_index][column_index - 1] <= cell:
                    continue

            # Check right
            if column_index < len(row) - 1:
                if heightmap[row_index][column_index + 1] <= cell:
                    continue

            risk_level = cell + 1
            total_risk_level += risk_level

    print(f"Total risk level = {total_risk_level}")
