from __future__ import annotations

from itertools import chain
from pathlib import Path

from helpers import clean_line
from helpers import transpose_2d_array
from helpers.logger import get_logger

LOGGER = get_logger("2021-day-04")


def read_input(filename: Path | str) -> tuple[list[int], list[list[list[int]]]]:
    numbers: list[int] = []
    bingo_boards: list[list[list[int]]] = []
    current_board: list[list[int]] = []

    with Path(filename).open(encoding="utf-8") as lines:
        for line in lines:
            if len(clean_line(line).strip()) == 0:
                continue

            if not numbers:
                numbers.extend([int(value) for value in clean_line(line).split(",")])
                continue

            current_board.append(
                [int(value) for value in line.split(" ") if len(value.strip()) > 0],
            )

            if len(current_board) == 5:
                bingo_boards.append(current_board)
                current_board = []

    return numbers, bingo_boards


def update_board(bingo_board: list[list[int]], call_number: int) -> list[list[int]]:
    for row_index, row in enumerate(bingo_board):
        for column_index, cell in enumerate(row):
            if call_number == cell:
                bingo_board[row_index][column_index] = -1

    return bingo_board


def check_board(bingo_board: list[list[int]]) -> bool:
    return True if _check_rows(bingo_board) else bool(_check_columns(bingo_board))


def _check_rows(bingo_board: list[list[int]]) -> bool:
    return any(sum(row) == -5 for row in bingo_board)


def _check_columns(bingo_board: list[list[int]]) -> bool:
    return _check_rows(transpose_2d_array(bingo_board))


def sum_board(bingo_board: list[list[int]]) -> int:
    return sum(cell for cell in list(chain.from_iterable(bingo_board)) if cell > -1)


if __name__ == "__main__":
    # Part One
    call_numbers, original_boards = read_input("input.txt")
    boards = original_boards.copy()

    best_score: int = 0
    final_score: int = 0

    for number in call_numbers:
        for board in boards:
            update_board(board, number)

            if check_board(board):
                score = sum_board(board)

                if score > best_score:
                    best_score = score

        if best_score > 0:
            final_score = best_score * number
            break

    LOGGER.info("Best score is %d", final_score)

    # Part Two
    boards = original_boards.copy()
    winning_board_indices = set()
    losing_board_score: int = 0

    for number in call_numbers:
        for index, board in enumerate(boards):
            if index in winning_board_indices:
                continue

            update_board(board, number)

            if check_board(board):
                winning_board_indices.add(index)

                if len(winning_board_indices) == len(boards):
                    losing_board_score = sum_board(board) * number
                    break

        if losing_board_score > 0:
            break

    LOGGER.info("Losing score is %d", losing_board_score)
