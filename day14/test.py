from day14.main import apply_rules, evaluate_counts, get_distinct_characters, read_input


def test_day_14_read_input(sample_data):
    assert read_input("sample_input.txt") == sample_data


def test_apply_rules(sample_data):
    polymer_template, pair_insertion_rules = sample_data
    polymer_step_1 = apply_rules(polymer_template, pair_insertion_rules)

    assert polymer_step_1 == "NCNBCHB"

    polymer_step_2 = apply_rules(polymer_step_1, pair_insertion_rules)

    assert polymer_step_2 == "NBCCNBBBCBHCB"

    polymer_step_3 = apply_rules(polymer_step_2, pair_insertion_rules)

    assert polymer_step_3 == "NBBBCNCCNBBNBNBBCHBHHBCHB"

    polymer_step_4 = apply_rules(polymer_step_3, pair_insertion_rules)

    assert polymer_step_4 == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"


def test_evaluate_counts(sample_data):
    polymer, rules = sample_data
    characters = get_distinct_characters(polymer, rules)

    for _ in range(10):
        polymer = apply_rules(polymer, rules)

    (
        most_common_element,
        most_common_quantity,
        least_common_element,
        least_common_quantity,
    ) = evaluate_counts(polymer, characters)

    assert most_common_element == "B"
    assert most_common_quantity == 1749
    assert least_common_element == "H"
    assert least_common_quantity == 161
    assert most_common_quantity - least_common_quantity == 1588
