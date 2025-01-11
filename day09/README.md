This Python script analyzes biological sequence data from FASTA files. The program provides two types of analysis:

1. **Find the longest repeated sub-sequence** in the given sequence.
2. **Calculate the AT content** of the sequence, which measures the percentage of Adenine (A) and Thymine (T) bases in the sequence.

## Usage

- To find the **Longest Repeated Sub-sequence**:
   ```bash
   python analyze.py filename.fasta --duplicate

- To calculate the **AT Content**: 
   ```bash
   python analyze.py filename.fasta --atcontent

- To run both analyses (**longest repeated sub-sequence and AT content**):
     ```bash
    python analyze.py filename.fasta --duplicate --atcontent

