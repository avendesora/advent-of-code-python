from __future__ import annotations

from dataclasses import dataclass
from functools import cmp_to_key
from pathlib import Path
from typing import Any

from helpers import clean_line


@dataclass
class PacketPair:
    left: list[Any]
    right: list[Any]


def read_input(filename: Path | str) -> list[PacketPair]:
    packet_pairs: list[PacketPair] = []
    current_left = None
    current_right = None

    with open(filename, encoding="utf-8") as lines:
        for line in lines:
            line = clean_line(line)

            if line == "":
                packet_pairs.append(PacketPair(current_left or [], current_right or []))
                current_left = None
                current_right = None
                continue

            if current_left is None:
                current_left = eval(line)
                continue

            current_right = eval(line)

    packet_pairs.append(PacketPair(current_left or [], current_right or []))

    return packet_pairs


def is_correct_order(left: list[Any], right: list[Any]) -> bool | None:
    for index, left_item in enumerate(left):
        try:
            right_item = right[index]
        except IndexError:
            return False

        if isinstance(left_item, int):
            if isinstance(right_item, int):
                if left_item == right_item:
                    continue

                return left_item < right_item

            left_item = [left_item]

        if isinstance(right_item, int):
            right_item = [right_item]

        comparison = is_correct_order(left_item, right_item)

        if comparison is None:
            continue

        return comparison

    return None if len(left) == len(right) else True


def compare_packet(packet1: list[Any], packet2: list[Any]) -> int:
    comparison = is_correct_order(packet1, packet2)

    if comparison is None:
        return 0

    return -1 if comparison else 1


def part_one(input_data: list[PacketPair]) -> int:
    return sum(
        {
            index + 1
            for index, packet_pair in enumerate(input_data)
            if is_correct_order(packet_pair.left, packet_pair.right)
        },
    )


def part_two(input_data: list[PacketPair]) -> int:
    all_packets: list[Any] = []

    for packet_pair in input_data:
        all_packets.extend((packet_pair.left, packet_pair.right))

    divider_packet1 = [[2]]
    divider_packet2 = [[6]]
    all_packets.extend((divider_packet1, divider_packet2))

    sorted_packets = sorted(all_packets, key=cmp_to_key(compare_packet))

    divider_packet1_index = sorted_packets.index(divider_packet1) + 1
    divider_packet2_index = sorted_packets.index(divider_packet2) + 1

    return divider_packet1_index * divider_packet2_index


if __name__ == "__main__":
    day13_input = read_input("input.txt")
    print(part_one(day13_input))
    print(part_two(day13_input))
