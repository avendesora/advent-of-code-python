from __future__ import annotations

from pathlib import Path

from advent_of_code_2022.day07.models import Directory
from helpers import read_input_as_string_array


def read_input(filename: Path | str) -> list[str]:
    return read_input_as_string_array(filename)


def generate_directory_structure(input_data: list[str]) -> Directory:
    root = Directory("/")
    current_directory: Directory = root

    for line in input_data:
        if line.startswith("$"):
            full_command = line[2:]

            if full_command == "ls":
                continue

            command, parameter = full_command.split()

            if command != "cd":
                continue

            if parameter == "/":
                current_directory = root
            elif parameter == "..":
                current_directory = current_directory.parent or root
            else:
                current_directory.add_directory(parameter)
                current_directory = current_directory.sub_directories[parameter]
        elif line.startswith("dir "):
            _, directory_name = line.split()
            current_directory.add_directory(directory_name)
        else:
            file_size, file_name = line.split()
            current_directory.add_file(file_name, int(file_size))

    return root


def get_sizes(
    directory: Directory,
    sizes: dict[str, int] | None = None,
) -> dict[str, int]:
    if sizes is None:
        sizes = {}

    for child in directory.sub_directories.values():
        sizes = get_sizes(child, sizes)

    file_size = sum(file.size for file in directory.files.values())
    children_size = sum(
        child.total_size for child in directory.sub_directories.values()
    )
    directory.total_size = file_size + children_size

    sizes[directory.full_name] = directory.total_size

    return sizes


def part_one(sizes: dict[str, int]) -> int:
    return sum(size for size in sizes.values() if size <= 100000)


def part_two(root: Directory, sizes: dict[str, int]) -> int:
    return min(
        size
        for size in sizes.values()
        if size >= 30000000 - (70000000 - root.total_size)
    )


if __name__ == "__main__":
    day7_input = read_input("input.txt")
    root_directory = generate_directory_structure(day7_input)
    sizes_dict = get_sizes(root_directory)
    print(part_one(sizes_dict))
    print(part_two(root_directory, sizes_dict))
