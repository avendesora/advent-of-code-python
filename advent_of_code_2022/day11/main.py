from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import lcm
from pathlib import Path
from typing import Callable

from helpers import clean_line


@dataclass
class Monkey:
    monkey_id: int
    starting_items: list[int]
    operation: str
    operand: str
    test_divisor: int
    if_true: int
    if_false: int


def read_monkey_line(line: str) -> Monkey:
    _, monkey_id = line.split()
    return Monkey(
        monkey_id=int(monkey_id.replace(":", "")),
        starting_items=[],
        operation="",
        operand="",
        test_divisor=0,
        if_true=0,
        if_false=0,
    )


def read_starting_items_line(line: str) -> list[int]:
    return [int(item) for item in line.replace("Starting items: ", "").split(", ")]


def read_operation_line(line: str) -> tuple[str, str]:
    _, _, _, operation, operand = line.replace("Operation: ", "").split()
    return operation, operand


def read_input(filename: Path | str) -> dict[int, Monkey]:
    monkeys: dict[int, Monkey] = {}
    current_monkey = None

    with open(filename, encoding="utf-8") as lines:
        for line in lines:
            cleaned_line = clean_line(line)

            if cleaned_line.startswith("Monkey"):
                if current_monkey:
                    monkeys[current_monkey.monkey_id] = current_monkey

                current_monkey = read_monkey_line(cleaned_line)
                continue

            if not current_monkey:
                continue

            cleaned_line = cleaned_line.strip()

            if cleaned_line.startswith("Starting items: "):
                current_monkey.starting_items = read_starting_items_line(cleaned_line)
                continue

            if cleaned_line.startswith("Operation: "):
                current_monkey.operation, current_monkey.operand = read_operation_line(
                    cleaned_line
                )
                continue

            if cleaned_line.startswith("Test"):
                current_monkey.test_divisor = int(
                    cleaned_line.replace("Test: ", "").split()[-1]
                )
                continue

            if cleaned_line.startswith("If true"):
                current_monkey.if_true = int(
                    cleaned_line.replace("If true: ", "").split()[-1]
                )
                continue

            if cleaned_line.startswith("If false"):
                current_monkey.if_false = int(
                    cleaned_line.replace("If false: ", "").split()[-1]
                )
                continue

    if current_monkey:
        monkeys[current_monkey.monkey_id] = current_monkey

    return monkeys


@lru_cache
def test_item(operand1: int, operand2: int) -> bool:
    return operand1 % operand2 == 0


def run_inspections(
    monkeys: dict[int, Monkey],
    number_of_rounds: int,
    worry_level_reducer: Callable,
) -> int:
    max_monkey_number = max(monkeys.keys())
    monkey_inspection_counts: dict[int, int] = {
        monkey_number: 0 for monkey_number in range(max_monkey_number + 1)
    }

    for _ in range(number_of_rounds):
        for monkey_number in range(max_monkey_number + 1):
            monkey = monkeys.get(monkey_number)

            if not monkey:
                continue

            while monkey.starting_items:
                worry_level = monkey.starting_items.pop(0)

                operand = (
                    worry_level if monkey.operand == "old" else int(monkey.operand)
                )

                if monkey.operation == "*":
                    worry_level *= operand
                elif monkey.operation == "+":
                    worry_level += operand

                worry_level = worry_level_reducer(worry_level)
                test_result = test_item(worry_level, monkey.test_divisor)
                next_monkey_id = monkey.if_true if test_result else monkey.if_false
                next_monkey = monkeys.get(next_monkey_id)

                if not next_monkey:
                    continue

                next_monkey.starting_items.append(worry_level)
                monkeys[next_monkey_id] = next_monkey
                monkey_inspection_counts[monkey_number] += 1

    sorted_monkey_inspection_counts: list[int] = list(monkey_inspection_counts.values())
    sorted_monkey_inspection_counts.sort()

    return sorted_monkey_inspection_counts[-1] * sorted_monkey_inspection_counts[-2]


def part_one(monkeys: dict[int, Monkey]) -> int:
    return run_inspections(monkeys, 20, lambda x: x // 3)


def part_two(monkeys: dict[int, Monkey]) -> int:
    least_common_multiple = lcm(*{monkey.test_divisor for monkey in monkeys.values()})
    return run_inspections(monkeys, 10000, lambda x: x % least_common_multiple)


if __name__ == "__main__":
    day10_input = read_input("input.txt")
    print(part_one(day10_input))
    day10_input = read_input("input.txt")
    print(part_two(day10_input))
