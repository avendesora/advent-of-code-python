from dataclasses import dataclass
from pathlib import Path

from helpers import clean_line


@dataclass
class Test:
    test: str
    if_true: str
    if_false: str


@dataclass
class Monkey:
    monkey_id: int
    starting_items: list[int]
    operation: str
    test: Test


def read_input(filename: Path | str) -> dict[int, Monkey]:
    monkeys: dict[int, Monkey] = {}
    current_monkey = None

    with open(filename, encoding="utf-8") as lines:
        for line in lines:
            cleaned_line = clean_line(line)

            if cleaned_line.startswith("Monkey"):
                if current_monkey:
                    monkeys[current_monkey.monkey_id] = current_monkey

                _, monkey_id = cleaned_line.split()
                current_monkey = Monkey(
                    int(monkey_id.replace(":", "")), [], "", Test("", "", "")
                )
                continue

            if not current_monkey:
                continue

            cleaned_line = cleaned_line.strip()

            if cleaned_line.startswith("Starting items"):
                starting_items = [
                    int(item)
                    for item in cleaned_line.replace("Starting items: ", "").split(", ")
                ]
                current_monkey.starting_items = starting_items
                continue

            if cleaned_line.startswith("Operation"):
                current_monkey.operation = cleaned_line.replace("Operation: ", "")
                continue

            if cleaned_line.startswith("Test"):
                current_monkey.test.test = cleaned_line.replace("Test: ", "")
                continue

            if cleaned_line.startswith("If true"):
                current_monkey.test.if_true = cleaned_line.replace("If true: ", "")
                continue

            if cleaned_line.startswith("If false"):
                current_monkey.test.if_false = cleaned_line.replace("If false: ", "")
                continue

    if current_monkey:
        monkeys[current_monkey.monkey_id] = current_monkey

    return monkeys


def part_one(input_data: dict[int, Monkey]) -> int | None:
    monkeys = input_data.copy()
    max_monkey_number = max(monkeys.keys())
    monkey_inspection_counts: dict[int, int] = {}

    for round_number in range(10000):
        print(f"round {round_number}")

        for monkey_number in range(max_monkey_number + 1):
            monkey = monkeys.get(monkey_number)

            if not monkey:
                continue

            while monkey.starting_items:
                worry_level = monkey.starting_items.pop(0)
                _, _, _, operation, operand = monkey.operation.split()

                operand = worry_level if operand == "old" else int(operand)

                if operation == "*":
                    worry_level *= operand
                elif operation == "+":
                    worry_level += operand

                # worry_level = worry_level // 3

                test_value = monkey.test.test.split()[-1]
                test_result = worry_level % int(test_value) == 0

                next_monkey_id = int(monkey.test.if_true.split()[-1]) if test_result else int(monkey.test.if_false.split()[-1])
                next_monkey = monkeys.get(next_monkey_id)

                if not next_monkey:
                    continue

                next_monkey.starting_items.append(worry_level)
                monkeys[next_monkey_id] = next_monkey

                monkey_inspection_count = monkey_inspection_counts.get(monkey_number, 0)
                monkey_inspection_count += 1
                monkey_inspection_counts[monkey_number] = monkey_inspection_count

    sorted_monkey_inspection_counts: list[int] = list(monkey_inspection_counts.values())
    sorted_monkey_inspection_counts.sort()
    sorted_monkey_inspection_counts.reverse()

    monkey_business = sorted_monkey_inspection_counts[0] * sorted_monkey_inspection_counts[1]
    return monkey_business


def part_two(input_data: dict[int, Monkey]) -> int | None:
    return None


if __name__ == "__main__":
    day10_input = read_input("input.txt")
    print(part_one(day10_input))
    print(part_two(day10_input))
