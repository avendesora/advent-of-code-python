from functools import lru_cache
from statistics import mean, median, mode

from helpers import read_input_as_int_array_from_csv


def calculate_fuel(positions: list[int], target_position: int) -> int:
    fuel_consumption: int = 0

    for position in positions:
        fuel_consumption += abs(position - target_position)

    return fuel_consumption


def calculate_fuel2(positions: list[int], target_position: int) -> int:
    total_fuel_consumption: int = 0

    for position in positions:
        if position == target_position:
            continue

        distance: int = abs(position - target_position) + 1
        total_fuel_consumption += _get_fuel_consumption(distance)

    return total_fuel_consumption


@lru_cache(maxsize=None)
def _get_fuel_consumption(distance: int) -> int:
    return sum(range(distance))


if __name__ == "__main__":
    original_positions: list[int] = read_input_as_int_array_from_csv("input.txt")

    # Part One
    # mode_position: int = int(mode(original_positions))
    # print(
    #     f"It will take {calculate_fuel(original_positions, mode_position)} fuel to align to position {mode_position}."
    # )
    # mean_position: int = int(mean(original_positions))
    # print(
    #     f"It will take {calculate_fuel(original_positions, mean_position)} fuel to align to position {mean_position}."
    # )
    # median_position: int = int(median(original_positions))
    # print(
    #     f"It will take {calculate_fuel(original_positions, median_position)} fuel to align to position {median_position}."
    # )

    best_position: int = 0
    total_fuel: int = 0

    for target in range(max(original_positions)):
        fuel = calculate_fuel(original_positions, target)

        if total_fuel == 0 or fuel < total_fuel:
            best_position = target
            total_fuel = fuel

    print(f"Best position = {best_position}, Fuel consumption = {total_fuel}.")

    # Looks like median is the best. (For Part One)

    # Part Two
    # mode_position = int(mode(original_positions))
    # print(
    #     f"It will take {calculate_fuel2(original_positions, mode_position)} fuel to align to position {mode_position}."
    # )
    # mean_position = int(mean(original_positions))
    # print(
    #     f"It will take {calculate_fuel2(original_positions, mean_position)} fuel to align to position {mean_position}."
    # )
    # median_position = int(median(original_positions))
    # print(
    #     f"It will take {calculate_fuel2(original_positions, median_position)} fuel to align to position {median_position}."
    # )

    best_position = 0
    total_fuel = 0

    for target in range(max(original_positions)):
        fuel = calculate_fuel2(original_positions, target)

        if total_fuel == 0 or fuel < total_fuel:
            best_position = target
            total_fuel = fuel

    print(f"Best position = {best_position}, Fuel consumption = {total_fuel}.")

    # Mean is best for this input, but that appears to be coincidental.
