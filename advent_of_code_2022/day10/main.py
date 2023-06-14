from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from helpers import read_input_as_string_array


@dataclass(eq=True, frozen=True)
class Operation:
    command: str
    value: int


def read_input(filename: Path | str) -> list[Operation]:
    lines = read_input_as_string_array(filename)
    operations: list[Operation] = []

    for line in lines:
        if line == "noop":
            operations.append(Operation("noop", 0))
            continue

        command, value = line.split()
        operations.append(Operation(command, int(value)))

    return operations


def run_cycle(
    get_next: bool,
    index: int,
    x: int,
    operations: list[Operation],
) -> tuple[bool, int, int]:
    if get_next:
        return operations[index + 1].command == "noop", index + 1, x

    return True, index, x + operations[index].value


def part_one(input_data: list[Operation]) -> int:
    x: int = 1
    get_next: bool = True
    index: int = -1
    signal_strengths: list[int] = []

    for cycle in range(220):
        if (cycle + 21) % 40 == 0:
            signal_strengths.append((cycle + 1) * x)

        get_next, index, x = run_cycle(get_next, index, x, input_data)

    return sum(signal_strengths)


def part_two(input_data: list[Operation]) -> list[str]:
    x: int = 1
    get_next: bool = True
    index: int = -1
    pixels: str = ""

    for cycle in range(240):
        pixels += "#" if cycle % 40 in {x, x - 1, x + 1} else "."
        get_next, index, x = run_cycle(get_next, index, x, input_data)

    return [pixels[i : i + 40] for i in range(0, len(pixels), 40)]


if __name__ == "__main__":
    day10_input = read_input("input.txt")
    print(part_one(day10_input))
    print()

    for crt_line in part_two(day10_input):
        print(crt_line.replace(".", " "))
