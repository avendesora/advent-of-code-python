from __future__ import annotations

from pathlib import Path

from helpers import read_input_as_2d_int_array


def read_input(filename: Path | str) -> list[list[int]]:
    return read_input_as_2d_int_array(filename)


def get_views(
    input_data: list[list[int]],
    row: list[int],
    row_index: int,
    column_index: int,
) -> tuple[list[int], list[int], list[int], list[int]]:
    left = row[:column_index]
    right = row[column_index + 1 :]
    top = []
    bottom = []

    for index, row in enumerate(input_data):
        if index < row_index:
            top.append(row[column_index])
            continue

        if index == row_index:
            continue

        bottom.append(row[column_index])

    return left, right, top, bottom


def get_scenic_score(view: list[int], current_height: int) -> int:
    return next(
        (
            index + 1
            for index, tree_height in enumerate(view)
            if tree_height >= current_height
        ),
        len(view),
    )


def part_one(input_data: list[list[int]]) -> int:
    visible_count = 0

    for row_index, row in enumerate(input_data):
        for column_index, cell in enumerate(row):
            if row_index in {0, len(input_data) - 1}:
                visible_count += 1
                continue

            if column_index in {0, len(row) - 1}:
                visible_count += 1
                continue

            left, right, top, bottom = get_views(
                input_data,
                row,
                row_index,
                column_index,
            )

            if min([max(left), max(right), max(top), max(bottom)]) < cell:
                visible_count += 1

    return visible_count


def part_two(input_data: list[list[int]]) -> int:
    scenic_scores: list[int] = []

    for row_index, row in enumerate(input_data):
        for column_index, cell in enumerate(row):
            left, right, top, bottom = get_views(
                input_data,
                row,
                row_index,
                column_index,
            )

            left.reverse()
            top.reverse()

            left_score = get_scenic_score(left, cell)
            right_score = get_scenic_score(right, cell)
            top_score = get_scenic_score(top, cell)
            bottom_score = get_scenic_score(bottom, cell)

            scenic_scores.append(left_score * right_score * top_score * bottom_score)

    return max(scenic_scores)


if __name__ == "__main__":
    day8_input = read_input("input.txt")
    print(part_one(day8_input))
    print(part_two(day8_input))
