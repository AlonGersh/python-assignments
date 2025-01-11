import argparse
from collections import defaultdict

def parse_fasta(file_path):
    """
    Parse a Fasta file and return a dictionary with sequence IDs as keys and sequences as values.
    """
    sequences = {}
    with open(file_path, 'r') as file:
        current_seq_id = None
        current_seq = []
        
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_seq_id:
                    sequences[current_seq_id] = ''.join(current_seq)
                current_seq_id = line[1:]
                current_seq = []
            else:
                current_seq.append(line)
        if current_seq_id:
            sequences[current_seq_id] = ''.join(current_seq)
    
    return sequences

def find_longest_duplicate(sequence):
    """
    Find the longest repeated sub-sequence in the given sequence.
    """
    n = len(sequence)
    longest_subseq = ""
    
    # Use a dictionary to store substrings and their positions
    substrings = defaultdict(list)
    
    for length in range(1, n // 2 + 1):
        for i in range(n - length + 1):
            subseq = sequence[i:i+length]
            substrings[subseq].append(i)
            
    # Find the longest subsequence that appears more than once
    for subseq, positions in substrings.items():
        if len(positions) > 1 and len(subseq) > len(longest_subseq):
            longest_subseq = subseq
    
    return longest_subseq

def calculate_at_content(sequence):
    """
    Calculate the AT content of a sequence.
    """
    at_count = sum(1 for base in sequence if base in "AT")
    return (at_count / len(sequence)) * 100

def analyze_file(file_path, find_duplicates=False, calculate_at=False):
    """
    Perform sequence analysis on a file and print results based on user options.
    """
    sequences = parse_fasta(file_path)
    
    for seq_id, sequence in sequences.items():
        print(f"Analyzing sequence: {seq_id}")
        
        if find_duplicates:
            print("Longest repeated sub-sequence:", find_longest_duplicate(sequence))
        
        if calculate_at:
            print(f"AT Content: {calculate_at_content(sequence):.2f}%")
        
        print("-" * 40)

def main():
    parser = argparse.ArgumentParser(description="Analyze sequences in a Fasta or GeneBank file.")
    parser.add_argument("file", help="Path to the input file (Fasta or GeneBank format).")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest repeated sub-sequence.")
    parser.add_argument("--atcontent", action="store_true", help="Analyze AT content of the sequence.")
    
    args = parser.parse_args()
    
    analyze_file(args.file, 
                 find_duplicates=args.duplicate, 
                 calculate_at=args.atcontent)

if __name__ == "__main__":
    main()
