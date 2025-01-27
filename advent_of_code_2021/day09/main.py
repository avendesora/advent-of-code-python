from __future__ import annotations

from functools import reduce

from helpers import read_input_as_2d_int_array
from helpers.logger import get_logger

LOGGER = get_logger("2021-day-08")


def get_risk_level(point_array: list[list[int]]) -> int:
    total_risk_level: int = 0

    for row_index, row in enumerate(point_array):
        for column_index, cell in enumerate(row):
            # Check above
            if row_index > 0 and point_array[row_index - 1][column_index] <= cell:
                continue

            # Check below
            if (
                row_index < len(point_array) - 1
                and point_array[row_index + 1][column_index] <= cell
            ):
                continue

            # Check left
            if column_index > 0 and row[column_index - 1] <= cell:
                continue

            # Check right
            if column_index < len(row) - 1 and row[column_index + 1] <= cell:
                continue

            risk_level = cell + 1
            total_risk_level += risk_level

    return total_risk_level


def get_basins(point_array: list[list[int]]) -> list[set[str]]:
    basin_list: list[set[str]] = []
    processed_cells: set[str] = set()

    for row_index, row in enumerate(point_array):
        for column_index, cell in enumerate(row):
            # If value is 9, not in a basin
            if cell == 9:
                continue

            cell_id = f"{row_index}|{column_index}"

            if cell_id in processed_cells:
                continue

            current_basin_set = get_basin(point_array, row_index, column_index, set())
            processed_cells = processed_cells.union(current_basin_set)
            basin_list.append(current_basin_set)

    return basin_list


def get_basin(
    point_array: list[list[int]],
    row_index: int,
    column_index: int,
    current_basin: set[str],
) -> set[str]:
    # Check above
    if row_index > 0 and point_array[row_index - 1][column_index] < 9:
        cell_id = f"{row_index - 1}|{column_index}"

        if cell_id not in current_basin:
            current_basin.add(cell_id)
            current_basin = get_basin(
                point_array,
                row_index - 1,
                column_index,
                current_basin,
            )

    # Check below
    if (
        row_index < len(point_array) - 1
        and point_array[row_index + 1][column_index] < 9
    ):
        cell_id = f"{row_index + 1}|{column_index}"

        if cell_id not in current_basin:
            current_basin.add(cell_id)
            current_basin = get_basin(
                point_array,
                row_index + 1,
                column_index,
                current_basin,
            )

    # Check left
    if column_index > 0 and point_array[row_index][column_index - 1] < 9:
        cell_id = f"{row_index}|{column_index - 1}"

        if cell_id not in current_basin:
            current_basin.add(cell_id)
            current_basin = get_basin(
                point_array,
                row_index,
                column_index - 1,
                current_basin,
            )

    # Check right
    if (
        column_index < len(point_array[0]) - 1
        and point_array[row_index][column_index + 1] < 9
    ):
        cell_id = f"{row_index}|{column_index + 1}"

        if cell_id not in current_basin:
            current_basin.add(cell_id)
            current_basin = get_basin(
                point_array,
                row_index,
                column_index + 1,
                current_basin,
            )

    return current_basin


def get_product_size(basin_list: list[set[str]], number_of_basins: int) -> int:
    basin_lengths: list[int] = [len(basin_set) for basin_set in basin_list]
    basin_lengths.sort()

    if len(basin_lengths) > number_of_basins:
        basin_lengths = basin_lengths[-number_of_basins:]

    return reduce((lambda x, y: x * y), basin_lengths)


if __name__ == "__main__":
    height_map: list[list[int]] = read_input_as_2d_int_array("input.txt")

    # Part One
    LOGGER.info("Total risk level = %d", get_risk_level(height_map))

    # Part Two
    basins: list[set[str]] = get_basins(height_map)
    product: int = get_product_size(basins, 3)

    LOGGER.info("The product of the sizes of the three largest basins is %d.", product)
