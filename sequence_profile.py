#!/usr/bin/env python3
"""
Sequence Profile Generator

Generates position-specific scoring matrices (PSSM) from multiple sequence alignments
and exports them as CSV files.
"""

import sys
import os
from pathlib import Path
from Bio import AlignIO
import pandas as pd

# Configuration
OUTPUT_PREFIX = os.environ.get('MSA_OUTPUT_PREFIX', 'sequence_analysis')
SCRIPT_DIR = Path(__file__).resolve().parent


def calculate_sequence_profiles(alignment_file):
    """
    Calculate position-specific probability matrix from MSA.
    
    Args:
        alignment_file: Path to FASTA file with aligned sequences
        
    Returns:
        DataFrame with probability matrix (positions x amino acids)
    """
    # Read alignment
    alignment = AlignIO.read(alignment_file, "fasta")
    
    # Get alignment dimensions
    num_sequences = len(alignment)
    alignment_length = alignment.get_alignment_length()
    
    # Get all unique characters in the alignment
    all_chars = set()
    for record in alignment:
        all_chars.update(str(record.seq))
    
    # Sort characters for consistent ordering
    sorted_chars = sorted(list(all_chars))
    
    # Initialize count matrix
    count_matrix = {char: [0] * alignment_length for char in sorted_chars}
    
    # Count occurrences at each position
    for position in range(alignment_length):
        for record in alignment:
            char = str(record.seq)[position]
            count_matrix[char][position] += 1
    
    # Convert counts to probabilities
    prob_matrix = {}
    for char in sorted_chars:
        prob_matrix[char] = [count / num_sequences for count in count_matrix[char]]
    
    # Create DataFrame
    df = pd.DataFrame(prob_matrix)
    df.index.name = 'Position'
    
    return df


def main():
    if len(sys.argv) != 2:
        print("Usage: python sequence_profile.py <alignment_file.fasta>")
        sys.exit(1)
    
    alignment_file = sys.argv[1]
    
    # Calculate sequence profile
    profile_df = calculate_sequence_profiles(alignment_file)
    
    # Save to CSV
    output_csv = SCRIPT_DIR / f"{OUTPUT_PREFIX}_sequence_profile.csv"
    profile_df.to_csv(output_csv)
    
    print(f"Sequence profile saved to: {output_csv}")


if __name__ == "__main__":
    main()
