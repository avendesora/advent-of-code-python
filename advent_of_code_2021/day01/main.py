from __future__ import annotations

from helpers import read_input_as_int_array
from helpers.logger import get_logger

LOGGER = get_logger("2021-day-01")


def count_larger_depths(depth_numbers: list[int]) -> int:
    if len(depth_numbers) < 2:
        return 0

    larger_depth_count: int = 0
    previous_depth = depth_numbers[0]

    for depth in depth_numbers[1:]:
        if depth > previous_depth:
            larger_depth_count += 1

        previous_depth = depth

    return larger_depth_count


def apply_sliding_window(depth_numbers: list[int], window_size: int) -> list[int]:
    sums: list[int] = []

    for depth in depth_numbers:
        sums.append(depth)

        for window in range(1, window_size):
            if window < len(sums):
                sums[-(window + 1)] += depth

    return sums[: -(window_size - 1)]


if __name__ == "__main__":
    # Part One
    depths: list[int] = read_input_as_int_array("input.txt")
    LOGGER.info("The depth increased %d times.", count_larger_depths(depths))

    # Part Two
    depth_sums: list[int] = apply_sliding_window(depths, 3)
    LOGGER.info(
        "The depth (using a sliding window) increased %d times.",
        count_larger_depths(depth_sums),
    )
