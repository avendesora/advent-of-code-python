from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from helpers import read_input_as_string_array
from helpers.logger import get_logger

if TYPE_CHECKING:
    from pathlib import Path

LOGGER = get_logger("2022-day-16")


@dataclass(eq=True, frozen=True)
class Valve:
    name: str
    flow_rate: int
    tunnels: list[str]

    def __hash__(self: Valve) -> int:
        return hash(self.name)


@dataclass(eq=True, frozen=True)
class State:
    open_valves: set[Valve]
    current_valve: Valve
    pressure_released: int
    current_elephant_valve: Valve | None = None

    def __hash__(self: State) -> int:
        return hash((str(self.open_valves), self.current_valve, self.pressure_released))

    def current_flow_rate(self: State) -> int:
        return sum(valve.flow_rate for valve in self.open_valves)


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


def _create_state_stay_put(state: State) -> State:
    return State(
        open_valves=state.open_valves,
        current_valve=state.current_valve,
        pressure_released=state.pressure_released + state.current_flow_rate(),
        current_elephant_valve=state.current_elephant_valve,
    )


def _create_state_open_valve(
    state: State,
    valve: Valve,
    increase_pressure_released: bool = True,
    offset: int = 0,
) -> State | None:
    if valve is None:
        return None

    if valve in state.open_valves:
        return None

    if valve.flow_rate == 0:
        return None

    return State(
        open_valves=state.open_valves | {valve},
        current_valve=state.current_valve,
        pressure_released=(
            state.pressure_released + state.current_flow_rate() - offset
            if increase_pressure_released
            else state.pressure_released
        ),
        current_elephant_valve=state.current_elephant_valve,
    )


def _create_state_move_down_tunnel(
    state: State,
    tunnel_valve: Valve,
    increase_pressure_released: bool = True,
) -> State:
    return State(
        open_valves=state.open_valves,
        current_valve=tunnel_valve,
        pressure_released=(
            state.pressure_released + state.current_flow_rate()
            if increase_pressure_released
            else state.pressure_released
        ),
        current_elephant_valve=state.current_elephant_valve,
    )


PRUNE_ZERO_OPEN_VALVE_MINUTES: int = 5
PRUNE_ONE_OPEN_VALVE_MINUTES: int = 10
PRUNE_TWO_OPEN_VALVE_MINUTES: int = 14
PRUNE_THREE_OPEN_VALVE_MINUTES: int = 18
PRUNE_FOUR_OPEN_VALVE_MINUTES: int = 22
PRUNE_FIVE_OPEN_VALVE_MINUTES: int = 25


def _should_prune_state(state: State, minute: int) -> bool:
    number_of_open_valves = len(state.open_valves)

    return (
        (minute > PRUNE_ZERO_OPEN_VALVE_MINUTES and number_of_open_valves == 0)
        or (minute > PRUNE_ONE_OPEN_VALVE_MINUTES and number_of_open_valves == 1)
        or (minute > PRUNE_TWO_OPEN_VALVE_MINUTES and number_of_open_valves == 2)
        or (minute > PRUNE_THREE_OPEN_VALVE_MINUTES and number_of_open_valves == 3)
        or (minute > PRUNE_FOUR_OPEN_VALVE_MINUTES and number_of_open_valves == 4)
        or (minute > PRUNE_FIVE_OPEN_VALVE_MINUTES and number_of_open_valves == 5)
    )


def part_one(input_data: list[Valve]) -> int:
    all_valves: dict[str, Valve] = {valve.name: valve for valve in input_data}
    max_flow_rate: int = sum(valve.flow_rate for valve in input_data)
    states: set[State] = {
        State(
            open_valves=set(),
            current_valve=all_valves["AA"],
            pressure_released=0,
        ),
    }
    total_minutes: int = 30
    current_max_pressure_released: int = 0
    max_flow_rate_achieved: bool = False

    for minute in range(1, total_minutes + 1):
        LOGGER.debug("Minute %s", minute)
        LOGGER.debug("Number of States: %d", len(states))
        new_states: set[State] = set()

        for state in states:
            # Prune if no open valves for a while.
            if _should_prune_state(state, minute):
                continue

            # If we've hit the max flow rate, stop branching and stick with this state.
            if state.current_flow_rate() == max_flow_rate:
                stay_put_state = _create_state_stay_put(state)

                # Don't continue with this state if it can't beat the current max.
                if (
                    max_flow_rate_achieved
                    and current_max_pressure_released > stay_put_state.pressure_released
                ):
                    continue

                max_flow_rate_achieved = True
                current_max_pressure_released = stay_put_state.pressure_released
                new_states.add(stay_put_state)
                continue

            open_valve_state = _create_state_open_valve(state, state.current_valve)

            # Don't continue with this state if it can't beat the current max.
            if open_valve_state and (
                open_valve_state.pressure_released > current_max_pressure_released
                or not max_flow_rate_achieved
            ):
                new_states.add(open_valve_state)

            # Create a new state for each of the current valve's tunnels.
            for tunnel in state.current_valve.tunnels:
                tunnel_valve = all_valves[tunnel]
                tunnel_state = _create_state_move_down_tunnel(state, tunnel_valve)

                # Don't continue with this state if it can't beat the current max.
                if (
                    tunnel_state.pressure_released > current_max_pressure_released
                    or not max_flow_rate_achieved
                ):
                    new_states.add(tunnel_state)

        states = new_states

    return max(state.pressure_released for state in states)


def _create_state_move_down_tunnel_elephant(
    state: State,
    tunnel_valve: Valve,
    offset: int = 0,
) -> State:
    return State(
        open_valves=state.open_valves,
        current_valve=state.current_valve,
        pressure_released=state.pressure_released + state.current_flow_rate() - offset,
        current_elephant_valve=tunnel_valve,
    )


def _create_elephant_states(
    state: State,
    all_valves: dict[str, Valve],
    max_flow_rate_achieved: bool,
    current_max_pressure_released: int,
    offset: int = 0,
) -> set[State]:
    new_states: set[State] = set()

    if state.current_elephant_valve is None:
        return new_states

    # Open the elephant's valve
    if state.current_valve != state.current_elephant_valve:
        open_valve_state = _create_state_open_valve(
            state,
            state.current_elephant_valve,
            True,
            offset,
        )

        if (
            open_valve_state
            and (
                open_valve_state.pressure_released > current_max_pressure_released
                or not max_flow_rate_achieved
            )
            and (
                current_max_pressure_released == 0
                or current_max_pressure_released < open_valve_state.pressure_released
            )
        ):
            new_states.add(open_valve_state)

    # Move the elephant down the tunnel(s)
    for tunnel in state.current_elephant_valve.tunnels:
        tunnel_valve = all_valves[tunnel]
        tunnel_state = _create_state_move_down_tunnel_elephant(
            state,
            tunnel_valve,
            offset,
        )

        # Don't continue with this state if it can't beat the current max.
        if (
            tunnel_state.pressure_released > current_max_pressure_released
            or not max_flow_rate_achieved
        ) and (
            current_max_pressure_released == 0
            or current_max_pressure_released < tunnel_state.pressure_released
        ):
            new_states.add(tunnel_state)

    return new_states


def _should_prune_state2(state: State, minute: int) -> bool:
    number_of_open_valves = len(state.open_valves)

    return (
        (minute > 4 and number_of_open_valves == 0)
        or (minute > 8 and number_of_open_valves == 1)
        or (minute > 11 and number_of_open_valves == 2)
        or (minute > 14 and number_of_open_valves == 3)
        or (minute > 16 and number_of_open_valves == 4)
        or (minute > 18 and number_of_open_valves == 5)
        or (minute > 20 and number_of_open_valves == 6)
        or (minute > 22 and number_of_open_valves == 7)
        or (minute > 24 and number_of_open_valves == 8)
    )


def part_two(input_data: list[Valve]) -> int | None:
    all_valves: dict[str, Valve] = {valve.name: valve for valve in input_data}
    max_flow_rate: int = sum(valve.flow_rate for valve in input_data)
    states: set[State] = {
        State(
            open_valves=set(),
            current_valve=all_valves["AA"],
            pressure_released=0,
            current_elephant_valve=all_valves["AA"],
        ),
    }
    total_minutes: int = 26
    current_max_pressure_released: int = 0
    max_flow_rate_achieved: bool = False

    for minute in range(1, total_minutes + 1):
        LOGGER.debug("Minute %s", minute)
        LOGGER.debug("Number of States: %d", len(states))
        new_states: set[State] = set()

        for state in states:
            # If we've hit the max flow rate, stop branching and stick with this state.
            if state.current_flow_rate() == max_flow_rate:
                stay_put_state = _create_state_stay_put(state)

                # Don't continue with this state if it can't beat the current max.
                if (
                    max_flow_rate_achieved
                    and current_max_pressure_released > stay_put_state.pressure_released
                ):
                    continue

                max_flow_rate_achieved = True
                current_max_pressure_released = stay_put_state.pressure_released
                new_states.add(stay_put_state)
                continue

            # Prune if no open valves for a while.
            if _should_prune_state2(state, minute):
                continue

            if open_valve_state := _create_state_open_valve(
                state,
                state.current_valve,
                False,
            ):
                new_states.update(
                    _create_elephant_states(
                        open_valve_state,
                        all_valves,
                        max_flow_rate_achieved,
                        current_max_pressure_released,
                        open_valve_state.current_valve.flow_rate,
                    ),
                )

            # Create a new state for each of the current valve's tunnels.
            for tunnel in state.current_valve.tunnels:
                tunnel_valve = all_valves[tunnel]
                tunnel_state = _create_state_move_down_tunnel(
                    state,
                    tunnel_valve,
                    False,
                )
                new_states.update(
                    _create_elephant_states(
                        tunnel_state,
                        all_valves,
                        max_flow_rate_achieved,
                        current_max_pressure_released,
                    ),
                )

        states = new_states

        if minute > 10:
            current_max_pressure_released = max(
                state.pressure_released for state in states
            )

    return max(state.pressure_released for state in states)


if __name__ == "__main__":
    day16_input = read_input("input.txt")
    LOGGER.info(part_one(day16_input))
    LOGGER.info(part_two(day16_input))
