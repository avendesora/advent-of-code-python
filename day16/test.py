from day16.main import convert_hex_to_binary
from day16.main import get_literal_value
from day16.main import parse_packets
from day16.main import part_one
from day16.main import part_two
from day16.main import read_input


def test_day_16_read_input() -> None:
    binary_data = read_input("sample_input.txt")
    assert binary_data == "110100101111111000101000"


def test_day_16_read_input2() -> None:
    binary_data = read_input("sample_input2.txt")
    assert binary_data == "00111000000000000110111101000101001010010001001000000000"


def test_day_16_get_literal_value() -> None:
    binary_data = "101111111000101000"
    literal_value, updated_binary_data = get_literal_value(binary_data, True)
    assert literal_value == 2021
    assert updated_binary_data == ""


def test_day_16_parse_packets() -> None:
    binary_data = read_input("sample_input2.txt")
    packets, _ = parse_packets(binary_data)

    assert packets is not None
    assert len(packets) == 1

    root_packet = packets[0]

    assert root_packet.sub_packets is not None
    assert len(root_packet.sub_packets) == 2
    assert root_packet.sub_packets[0].literal_value == 10
    assert root_packet.sub_packets[1].literal_value == 20


def test_day_16_parse_more_packets() -> None:
    binary_data = read_input("sample_input3.txt")
    packets, _ = parse_packets(binary_data)

    assert packets is not None
    assert len(packets) == 1

    root_packet = packets[0]

    assert root_packet.sub_packets is not None
    assert len(root_packet.sub_packets) == 3
    assert root_packet.sub_packets[0].literal_value == 1
    assert root_packet.sub_packets[1].literal_value == 2
    assert root_packet.sub_packets[2].literal_value == 3


def test_day_16_part_one() -> None:
    binary_data = read_input("sample_input4.txt")
    result = part_one(binary_data)
    assert result == 16

    binary_data = read_input("sample_input5.txt")
    result = part_one(binary_data)
    assert result == 12

    binary_data = read_input("sample_input6.txt")
    result = part_one(binary_data)
    assert result == 23

    binary_data = read_input("sample_input7.txt")
    result = part_one(binary_data)
    assert result == 31


def test_day_16_part_two() -> None:
    binary_data = convert_hex_to_binary("C200B40A82")
    result = part_two(binary_data)
    assert result == 3

    binary_data = convert_hex_to_binary("04005AC33890")
    result = part_two(binary_data)
    assert result == 54

    binary_data = convert_hex_to_binary("880086C3E88112")
    result = part_two(binary_data)
    assert result == 7

    binary_data = convert_hex_to_binary("CE00C43D881120")
    result = part_two(binary_data)
    assert result == 9

    binary_data = convert_hex_to_binary("D8005AC2A8F0")
    result = part_two(binary_data)
    assert result == 1

    binary_data = convert_hex_to_binary("F600BC2D8F")
    result = part_two(binary_data)
    assert result == 0

    binary_data = convert_hex_to_binary("9C005AC2F8F0")
    result = part_two(binary_data)
    assert result == 0

    binary_data = convert_hex_to_binary("9C0141080250320F1802104A08")
    result = part_two(binary_data)
    assert result == 1
