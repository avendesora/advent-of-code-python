from helpers import read_input_as_2d_int_array


def take_step(energy_levels: list[list[int]]) -> list[list[int]]:
    for row_index, row in enumerate(energy_levels):
        for column_index, _ in enumerate(row):
            energy_levels[row_index][column_index] += 1

    for row_index, row in enumerate(energy_levels):
        for column_index, _ in enumerate(row):
            energy_levels = _flash(energy_levels, row_index, column_index)

    for row_index, row in enumerate(energy_levels):
        for column_index, cell in enumerate(row):
            if cell > 9:
                energy_levels[row_index][column_index] = 0

    return energy_levels


def _flash(
    energy_levels: list[list[int]],
    row_index: int,
    column_index: int,
) -> list[list[int]]:
    if energy_levels[row_index][column_index] != 10:
        return energy_levels

    energy_levels[row_index][column_index] += 1

    energy_levels = _increase_adjacent_cell(
        energy_levels,
        row_index - 1,
        column_index - 1,
    )
    energy_levels = _increase_adjacent_cell(
        energy_levels,
        row_index - 1,
        column_index,
    )
    energy_levels = _increase_adjacent_cell(
        energy_levels,
        row_index - 1,
        column_index + 1,
    )
    energy_levels = _increase_adjacent_cell(
        energy_levels,
        row_index,
        column_index - 1,
    )
    energy_levels = _increase_adjacent_cell(
        energy_levels,
        row_index,
        column_index + 1,
    )
    energy_levels = _increase_adjacent_cell(
        energy_levels,
        row_index + 1,
        column_index - 1,
    )
    energy_levels = _increase_adjacent_cell(
        energy_levels,
        row_index + 1,
        column_index,
    )
    return _increase_adjacent_cell(
        energy_levels,
        row_index + 1,
        column_index + 1,
    )


def _increase_adjacent_cell(
    energy_levels: list[list[int]],
    row_index: int,
    column_index: int,
) -> list[list[int]]:
    if row_index < 0 or column_index < 0:
        return energy_levels

    try:
        cell = energy_levels[row_index][column_index]
    except IndexError:
        return energy_levels

    if cell != 10:
        energy_levels[row_index][column_index] += 1

    return _flash(energy_levels, row_index, column_index)


def count_flashes(energy_levels: list[list[int]]) -> int:
    return sum(row.count(0) for row in energy_levels)


def take_steps(energy_levels: list[list[int]], steps: int) -> int:
    flashes = 0

    for _ in range(steps):
        energy_levels = take_step(energy_levels)
        flashes += count_flashes(energy_levels)

    return flashes


def find_first_simultaneous_flash(energy_levels: list[list[int]]) -> int:
    first_simultaneous_flash_step: int = -1
    step_count: int = 0

    while first_simultaneous_flash_step == -1:
        step_count += 1
        energy_levels = take_step(energy_levels)

        if count_flashes(energy_levels) == 100:
            first_simultaneous_flash_step = step_count

    return step_count


if __name__ == "__main__":
    # Part One
    number_of_steps: int = 100
    number_of_flashes: int = take_steps(
        read_input_as_2d_int_array("input.txt"), number_of_steps
    )
    print(
        f"After {number_of_steps} steps, there have been a total of "
        f"{number_of_flashes} flashes."
    )

    # Part Two
    first_flash = find_first_simultaneous_flash(read_input_as_2d_int_array("input.txt"))
    print(f"The first step at which all octopuses flash is {first_flash}.")
