from helpers import read_input_as_int_array_from_csv


def grow_one_day(initial_school: list[int]) -> list[int]:
    updated_school: list[int] = []
    new_school: list[int] = []

    for fish in initial_school:
        if fish > 0:
            updated_school.append(fish - 1)
            continue

        updated_school.append(8)
        new_school.append(6)

    return updated_school + new_school


def initialize_school_dict(initial_school: list[int]) -> dict[int, int]:
    initial_school_dict: dict[int, int] = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }

    for fish in initial_school:
        initial_school_dict[fish] += 1

    return initial_school_dict


def update_school_dict(current_school_dict: dict[int, int]) -> dict[int, int]:
    updated_school_dict: dict[int, int] = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }

    for key, value in current_school_dict.items():
        if key == 0:
            updated_school_dict[6] += value
            updated_school_dict[8] += value
            continue

        updated_school_dict[key - 1] += value

    return updated_school_dict


if __name__ == "__main__":
    original_school = read_input_as_int_array_from_csv("input.txt")

    # Part One
    school = original_school.copy()
    # print(f"Initial state: {school}")

    number_of_days = 80

    for day in range(number_of_days):
        school = grow_one_day(school)
        # print(f"After {day + 1} day(s): {school}")

    print(
        f"There are a total of {len(school)} fish in the school after {number_of_days} days."
    )

    # Part Two
    school_dict = initialize_school_dict(original_school)
    number_of_days2 = 256

    for day in range(number_of_days2):
        school_dict = update_school_dict(school_dict)
        # print(f"After {day + 1} days(s): {school_dict}")

    print(
        f"There are a total of {sum(school_dict.values())} fish in the school after {number_of_days2} days."
    )
