from seq import calculate_statistics

def test_statistics_a_seq():
    with open("a_seq.txt", "r") as file:
        sequence = file.read()

    expected_results = {
        "A": 2,
        "C": 5,
        "G": 6,
        "T": 7,
        "Unknown": 7,
    }
    expected_total = 27

    stats, total = calculate_statistics(sequence)

    for key in expected_results:
        assert stats[key][0] == expected_results[key]  

    assert total == expected_total


def test_statistics_b_seq():
    with open("b_seq.txt", "r") as file:
        sequence = file.read()

    expected_results = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4,
        "Unknown": 1,
    }
    expected_total = 11

    stats, total = calculate_statistics(sequence)

    for key in expected_results:
        assert stats[key][0] == expected_results[key]  
    
    assert total == expected_total