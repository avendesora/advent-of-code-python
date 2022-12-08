from __future__ import annotations

from dataclasses import dataclass
from math import prod
from pathlib import Path

from helpers import read_input_as_string_array


@dataclass
class Packet:
    version: int
    type_id: int
    literal_value: int | None
    sub_packets: list[Packet] | None


def read_input(filename: Path | str) -> str:
    input_string = read_input_as_string_array(filename)[0]
    return convert_hex_to_binary(input_string)


def convert_hex_to_binary(hex_string: str) -> str:
    chunks = [hex_string[i : i + 2] for i in range(0, len(hex_string), 2)]
    return "".join(["{:08b}".format(int(chunk, 16)) for chunk in chunks])


def parse_packets(
    binary_data: str,
    trim_bits: bool = True,
    count: int | None = None,
) -> tuple[list[Packet], str]:
    packets: list[Packet] = []

    while binary_data != "":
        try:
            packet_version, binary_data = get_packet_version(binary_data)
            packet_type_id, binary_data = get_packet_type_id(binary_data)
            literal_value = None
            sub_packets = None

            if packet_type_id == 4:
                literal_value, binary_data = get_literal_value(binary_data, trim_bits)
            else:
                sub_packets, binary_data = get_operator(binary_data)

            if literal_value or sub_packets:
                packets.append(
                    Packet(
                        packet_version,
                        packet_type_id,
                        literal_value,
                        sub_packets,
                    )
                )
        except (IndexError, ValueError):
            break

        if count and len(packets) == count:
            break

    return packets, binary_data


def get_packet_version(binary_data: str) -> tuple[int, str]:
    return int(binary_data[:3], 2), binary_data[3:]


def get_packet_type_id(binary_data: str) -> tuple[int, str]:
    return int(binary_data[:3], 2), binary_data[3:]


def get_literal_value(binary_data: str, trim_bits: bool) -> tuple[int, str]:
    start_index = 0
    literal_value_string = ""

    while True:
        indicator_bit = int(binary_data[start_index])

        start_index = start_index + 1
        end_index = start_index + 4

        literal_value_string += binary_data[start_index:end_index]
        start_index = end_index

        if indicator_bit == 0:
            break

    literal_value = int(literal_value_string, 2)

    if trim_bits:
        prefix_length = 6
        remainder = (start_index + prefix_length) % 4

        while remainder > 0:
            start_index += 1
            remainder = (start_index + prefix_length) % 4

    return literal_value, binary_data[start_index:]


def get_operator(binary_data: str) -> tuple[list[Packet], str]:
    length_type_id = int(binary_data[0])

    if length_type_id == 0:
        start_index = 16
        length = int(binary_data[1:start_index], 2)
        end_index = start_index + length
        sub_binary_data = binary_data[start_index:end_index]
        sub_packets, _ = parse_packets(sub_binary_data, trim_bits=False)
        binary_data = binary_data[end_index:]
    else:
        start_index = 12
        length = int(binary_data[1:start_index], 2)
        sub_binary_data = binary_data[start_index:]
        sub_packets, binary_data = parse_packets(
            sub_binary_data,
            trim_bits=False,
            count=length,
        )

    return sub_packets, binary_data


def sum_version_numbers(packets: list[Packet] | None) -> int:
    return (
        sum(
            packet.version + sum_version_numbers(packet.sub_packets)
            for packet in packets
        )
        if packets
        else 0
    )


def evaluate_packets(packet: Packet) -> int:
    if packet.type_id == 4:
        return packet.literal_value or 0

    if not packet.sub_packets:
        return 0

    if packet.type_id == 0:
        return sum(evaluate_packets(sub_packet) for sub_packet in packet.sub_packets)

    if packet.type_id == 1:
        return prod(evaluate_packets(sub_packet) for sub_packet in packet.sub_packets)

    if packet.type_id == 2:
        return min(evaluate_packets(sub_packet) for sub_packet in packet.sub_packets)

    if packet.type_id == 3:
        return max(evaluate_packets(sub_packet) for sub_packet in packet.sub_packets)

    if packet.type_id == 5:
        return (
            1
            if evaluate_packets(packet.sub_packets[0])
            > evaluate_packets(packet.sub_packets[1])
            else 0
        )

    if packet.type_id == 6:
        return (
            1
            if evaluate_packets(packet.sub_packets[0])
            < evaluate_packets(packet.sub_packets[1])
            else 0
        )

    if packet.type_id == 7:
        return (
            1
            if evaluate_packets(packet.sub_packets[0])
            == evaluate_packets(packet.sub_packets[1])
            else 0
        )

    return 0


def part_one(binary_data: str) -> int:
    packets, _ = parse_packets(binary_data)
    return sum_version_numbers(packets)


def part_two(binary_data: str) -> int:
    packets, _ = parse_packets(binary_data)
    return evaluate_packets(packets[0])


if __name__ == "__main__":
    binary_input: str = read_input("input.txt")
    print(part_one(binary_input))
    print(part_two(binary_input))
