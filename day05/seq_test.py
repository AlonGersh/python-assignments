from seq import calculate_statistics

def test_statistics_a_seq():
    # Read the content of a_seq.txt
    with open("a_seq.txt", "r") as file:
        sequence = file.read()

    expected_result = {
        "A": (2, 7.4),
        "C": (5, 18.5),
        "G": (6, 22.2),
        "T": (7, 25.9),
        "Unknown": (7, 25.9),
    }
    expected_total = 27

    stats, total = calculate_statistics(sequence)
    assert stats == expected_result
    assert total == expected_total

def test_statistics_b_seq():
    # Read the content of b_seq.txt
    with open("b_seq.txt", "r") as file:
        sequence = file.read()

    expected_result = {
        "A": (1, 9.1),
        "C": (2, 18.2),
        "G": (3, 27.3),
        "T": (4, 36.4),
        "Unknown": (1, 9.1),
    }
    expected_total = 11

    stats, total = calculate_statistics(sequence)
    assert stats == expected_result
    assert total == expected_total
