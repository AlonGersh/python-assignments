import sys
from collections import Counter

def compute_stats(sequence):
    """
    Compute the nucleotide statistics for a given sequence.
    """
    stats = Counter()
    total = 0

    for char in sequence:
        if char.upper() in "ACGT":
            stats[char.upper()] += 1
        else:
            stats["Unknown"] += 1
        total += 1

    return stats, total

def format_stats(stats, total):
    """
    Format the statistics for display.
    """
    output = []
    for base in "ACGT":
        count = stats[base]
        percentage = (count / total * 100) if total else 0
        output.append(f"{base}: {count:8d} {percentage:5.1f}%")
    
    unknown = stats["Unknown"]
    unknown_percentage = (unknown / total * 100) if total else 0
    output.append(f"Unknown: {unknown:5d} {unknown_percentage:5.1f}%")
    output.append(f"Total: {total:8d}")
    return "\n".join(output)

def process_file(file_path):
    """
    Process a single file to compute and display statistics.
    """
    with open(file_path, 'r') as file:
        sequence = file.read().replace("\n", "")
    stats, total = compute_stats(sequence)
    print(f"{file_path}")
    print(format_stats(stats, total))
    print()
    return stats, total

def main():
    if len(sys.argv) < 3:
        print("Usage: python seq.py <file1> <file2>")
        sys.exit(1)

    file1, file2 = sys.argv[1], sys.argv[2]

    # Process each file
    stats1, total1 = process_file(file1)
    stats2, total2 = process_file(file2)

    # Combine statistics
    combined_stats = stats1 + stats2
    combined_total = total1 + total2

    # Display combined statistics
    print("All")
    print(format_stats(combined_stats, combined_total))

if __name__ == "__main__":
    main()