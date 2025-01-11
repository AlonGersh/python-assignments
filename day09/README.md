# Sequence Analysis Tool

This Python script analyzes biological sequence data from FNA (or FASTA) files. The program provides two types of analysis:

1. **Find the longest repeated sub-sequence** in the given sequence.
2. **Calculate the AT content** of the sequence, which measures the percentage of Adenine (A) and Thymine (T) bases in the sequence.

## Features

- **Longest Repeated Sub-sequence**: Finds the longest subsequence that repeats at least twice in the sequence.
- **AT Content**: Calculates the percentage of A and T bases in the sequence.

## Requirements

- Python 3.x
- Biopython (for sequence parsing)

To install Biopython:
```bash
pip install biopython
