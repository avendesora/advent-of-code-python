from dataclasses import dataclass
from pathlib import Path

from helpers import read_input_as_string_array


@dataclass
class Instruction:
    count: int
    from_stack: int
    to_stack: int


def read_input(filename: Path | str) -> tuple[list[list[str]], list[Instruction]]:
    lines: list[str] = read_input_as_string_array(filename)
    instructions: list[Instruction] = []
    stack_dict: dict[int, list[str]] = {}

    for line in lines:
        if line.startswith("move "):
            line = line.replace("move ", "").replace("from ", "").replace("to ", "")
            count, from_stack, to_stack = line.split()
            instructions.append(Instruction(int(count), int(from_stack), int(to_stack)))
            continue

        max_number_of_letters = (len(line) + 1) // 4

        for index in range(1, max_number_of_letters + 1):
            crate_index = index * 4 - 3
            crate = line[crate_index]

            if crate == " " or crate.isnumeric():
                continue

            stack = stack_dict.get(index, [])
            stack.insert(0, crate)
            stack_dict[index] = stack

    stacks: list[list[str]] = [
        stack_dict.get(index, []) for index in range(1, max(stack_dict.keys()) + 1)
    ]

    return stacks, instructions


def get_top_crates(stacks: list[list[str]]) -> str:
    return "".join(stack[-1] for stack in stacks)


def part_one(stacks: list[list[str]], input_data: list[Instruction]) -> str:
    for instruction in input_data:
        from_stack = stacks[instruction.from_stack - 1]
        to_stack = stacks[instruction.to_stack - 1]

        for _ in range(instruction.count):
            to_stack.append(from_stack.pop())

    return get_top_crates(stacks)


def part_two(stacks: list[list[str]], input_data: list[Instruction]) -> str:
    for instruction in input_data:
        from_stack = stacks[instruction.from_stack - 1]
        to_stack = stacks[instruction.to_stack - 1]
        crates_to_move = [from_stack.pop() for _ in range(instruction.count)]
        crates_to_move.reverse()
        to_stack.extend(crates_to_move)

    return get_top_crates(stacks)


if __name__ == "__main__":
    starting_stacks, day5_input = read_input("input.txt")
    print(part_one(starting_stacks, day5_input))

    # re-read input since the stacks get modified in part one
    starting_stacks, day5_input = read_input("input.txt")
    print(part_two(starting_stacks, day5_input))
