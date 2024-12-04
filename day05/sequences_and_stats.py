import sys

def calculate_statistics(sequence):
    """
    Calculate statistics for a given sequence.
    """
    counts = {"A": 0, "C": 0, "G": 0, "T": 0, "Unknown": 0}
    total = len(sequence)
    
    for char in sequence:
        if char in counts:
            counts[char] += 1
        else:
            counts["Unknown"] += 1

    stats = {key: (counts[key], counts[key] / total * 100 if total > 0 else 0) for key in counts}
    return stats, total

def print_statistics(stats, total, label):
    """
    Print statistics for a single file or all files.
    """
    print(f"{label}")
    for key, (count, percentage) in stats.items():
        print(f"{key}: {count:>8} {percentage:6.1f}%")
    print(f"Total: {total:>6}")
    print()

def main():
    if len(sys.argv) != 3:
        print("Usage: python seq.py <file1> <file2>")
        return
    
    all_counts = {"A": 0, "C": 0, "G": 0, "T": 0, "Unknown": 0}
    total_all = 0

    for file_path in sys.argv[1:]:
        try:
            with open(file_path, "r") as file:
                sequence = file.read().strip()
                stats, total = calculate_statistics(sequence)
                print_statistics(stats, total, file_path)
                
                for key in all_counts:
                    all_counts[key] += stats[key][0]
                total_all += total
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return
        except Exception as e:
            print(f"An error occurred while processing {file_path}: {e}")
            return
    
    if total_all > 0:
        all_stats = {key: (all_counts[key], all_counts[key] / total_all * 100) for key in all_counts}
        print_statistics(all_stats, total_all, "All")

if __name__ == "__main__":
    main()