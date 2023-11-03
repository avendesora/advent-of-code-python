from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from helpers import read_input_as_string_array
from helpers.logger import get_logger

if TYPE_CHECKING:
    from pathlib import Path

LOGGER = get_logger("2022-day-16")


@dataclass
class Valve:
    name: str
    flow_rate: int
    tunnels: list[str]
    is_open: bool = False

    def __hash__(self: Valve) -> int:
        return hash(self.name)

    @property
    def flow_rate_value(self: Valve) -> int:
        return 0 if self.is_open else self.flow_rate


def read_input(filename: Path | str) -> list[Valve]:
    valves: list[Valve] = []

    for line in read_input_as_string_array(filename):
        name = line[6:8]
        flow_rate = int(line[line.index("=") + 1 : line.index(";")])

        try:
            tunnels = line[line.index("valves ") + 7 :].split(", ")
        except ValueError:
            tunnels = line[line.index("valve ") + 6 :].split(", ")

        valves.append(Valve(name, flow_rate, tunnels))

    return valves


def get_total_flow_rate(
    valve: Valve,
    valves: dict[str, Valve],
    open_valves: set[Valve],
    visited_valves: set[Valve] | None = None,
) -> int:
    if visited_valves is None:
        visited_valves = set()

    if valve in visited_valves:
        return 0

    visited_valves.add(valve)

    total_flow_rate = valve.flow_rate if valve not in open_valves else 0

    for child_valve_name in valve.tunnels:
        child_valve = valves.get(child_valve_name)

        if (
            child_valve is None
            or child_valve in open_valves
            or child_valve.flow_rate == 0
        ):
            continue

        total_flow_rate += get_total_flow_rate(
            child_valve,
            valves,
            open_valves,
            visited_valves,
        )

    return total_flow_rate


def should_move(
    valve: Valve,
    valves: dict[str, Valve],
    open_valves: set[Valve],
) -> bool:
    if valve in open_valves:
        return True

    max_unopened_child_flow_rate = 0

    for child_valve_name in valve.tunnels:
        child_valve = valves.get(child_valve_name)

        if child_valve is None or child_valve in open_valves:
            continue

        if child_valve.flow_rate > max_unopened_child_flow_rate:
            max_unopened_child_flow_rate = child_valve.flow_rate

    return max_unopened_child_flow_rate > valve.flow_rate


def part_one(input_data: list[Valve]) -> int:
    all_valves: dict[str, Valve] = {valve.name: valve for valve in input_data}
    open_valves: set[Valve] = set()
    current_valve: Valve = all_valves["AA"]
    minute = 1
    pressure_released = 0

    while minute <= 30:
        pressure_released += sum(valve.flow_rate for valve in open_valves)
        minute += 1

        if len(open_valves) == len(all_valves):
            continue

        if should_move(current_valve, all_valves, open_valves):
            highest_flow_rate: int = 0
            highest_tunnel_valves: set[Valve] = set()

            for valve_name in current_valve.tunnels:
                tunnel_valve = all_valves.get(valve_name)

                if tunnel_valve is None:
                    continue

                tunnel_valve_flow_rate = get_total_flow_rate(
                    tunnel_valve,
                    all_valves,
                    open_valves,
                )

                if tunnel_valve_flow_rate > highest_flow_rate:
                    highest_flow_rate = tunnel_valve_flow_rate
                    highest_tunnel_valves = {tunnel_valve}
                elif tunnel_valve_flow_rate == highest_flow_rate:
                    highest_tunnel_valves.add(tunnel_valve)

            highest_tunnel_valve = highest_tunnel_valves.pop()

            for tunnel_valve in highest_tunnel_valves:
                if tunnel_valve.flow_rate_value > highest_tunnel_valve.flow_rate_value:
                    highest_tunnel_valve = tunnel_valve

            current_valve = highest_tunnel_valve
        else:
            current_valve.is_open = True
            open_valves.add(current_valve)

    return pressure_released


def part_two(input_data: list[Valve]) -> int | None:
    LOGGER.debug(str(input_data))
    return None


if __name__ == "__main__":
    day16_input = read_input("input.txt")
    LOGGER.info(part_one(day16_input))
    LOGGER.info(part_two(day16_input))
