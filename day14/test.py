from day14.main import (
    apply_rules,
    evaluate_counts,
    evaluate_counts_part_two,
    get_character_counts,
    get_distinct_characters,
    get_pairs_from_polymer,
    read_input,
    update_pairs,
)


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


def test_get_pairs_from_polymer(sample_data, pairs):
    polymer, _ = sample_data
    actual_pairs = get_pairs_from_polymer(polymer)

    assert actual_pairs == pairs


def test_update_pairs(sample_data, pairs):
    polymer, rules = sample_data
    pairs0 = get_pairs_from_polymer(polymer)

    assert pairs0 == pairs

    pairs1 = update_pairs(pairs0, rules)

    assert pairs1 == get_pairs_from_polymer("NCNBCHB")

    pairs2 = update_pairs(pairs1, rules)

    assert pairs2 == get_pairs_from_polymer("NBCCNBBBCBHCB")

    pairs3 = update_pairs(pairs2, rules)

    assert pairs3 == get_pairs_from_polymer("NBBBCNCCNBBNBNBBCHBHHBCHB")

    pairs4 = update_pairs(pairs3, rules)

    assert pairs4 == get_pairs_from_polymer(
        "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    )


def test_get_character_counts(sample_data):
    polymer, rules = sample_data
    pairs = get_pairs_from_polymer(polymer)

    for _ in range(10):
        pairs = update_pairs(pairs, rules)

    character_counts = get_character_counts(pairs, polymer[-1])

    assert character_counts["B"] == 1749
    assert character_counts["C"] == 298
    assert character_counts["H"] == 161
    assert character_counts["N"] == 865


def test_get_character_counts_part_two(sample_data):
    polymer, rules = sample_data
    pairs = get_pairs_from_polymer(polymer)

    for _ in range(40):
        pairs = update_pairs(pairs, rules)

    character_counts = get_character_counts(pairs, polymer[-1])

    assert character_counts["B"] == 2192039569602
    assert character_counts["H"] == 3849876073


def test_evaluate_counts_part_two(sample_data):
    polymer, rules = sample_data
    pairs = get_pairs_from_polymer(polymer)

    for _ in range(40):
        pairs = update_pairs(pairs, rules)

    (
        most_common_element,
        most_common_quantity,
        least_common_element,
        least_common_quantity,
    ) = evaluate_counts_part_two(pairs, polymer)

    assert most_common_element == "B"
    assert most_common_quantity == 2192039569602
    assert least_common_element == "H"
    assert least_common_quantity == 3849876073
    assert most_common_quantity - least_common_quantity == 2188189693529
