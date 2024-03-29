from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


def read_input_as_int_array(filename: Path | str) -> list[int]:
    with Path(filename).open("r", encoding="utf-8") as lines:
        return [int(clean_line(line)) for line in lines if clean_line(line).isnumeric()]


def read_input_as_int_array_from_csv(filename: Path | str) -> list[int]:
    with Path(filename).open("r", encoding="utf-8") as file_lines:
        return [int(x) for x in file_lines.readline().split(",")]


def read_input_as_2d_int_array(filename: Path | str) -> list[list[int]]:
    input_2d_array: list[list[int]] = []

    with Path(filename).open("r", encoding="utf-8") as file_lines:
        for file_line in file_lines:
            clean_file_line = clean_line(file_line).strip()

            if len(clean_file_line) == 0:
                continue

            input_2d_array.append([int(character) for character in clean_file_line])

    return input_2d_array


def read_input_as_string_array(filename: Path | str) -> list[str]:
    with Path(filename).open("r", encoding="utf-8") as lines:
        return [clean_line(line) for line in lines if clean_line(line)]


def clean_line(file_line: str) -> str:
    return file_line.replace("\n", "")


def transpose_2d_array(input_array: list[list[Any]]) -> list[list[Any]]:
    return [list(x) for x in zip(*input_array)]


@dataclass
class Point2D:
    x: int
    y: int

    def __hash__(self: Point2D) -> int:
        return hash(f"{self.x},{self.y}")

    def __eq__(self: Point2D, other: object) -> bool:
        if not isinstance(other, Point2D):
            raise NotImplementedError

        return self.x == other.x and self.y == other.y
