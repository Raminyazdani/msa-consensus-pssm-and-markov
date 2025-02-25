import sys
from Bio.Align import MultipleSeqAlignment
import logomaker
from Bio import AlignIO
import csv
import os
import pandas as pd
from pathlib import Path

# Output file prefix - can be overridden via MSA_OUTPUT_PREFIX environment variable
OUTPUT_PREFIX = os.environ.get('MSA_OUTPUT_PREFIX', 'sequence_analysis')

# Get the project root directory (where this script is located)
SCRIPT_DIR = Path(__file__).resolve().parent


def calculate_sequence_profiles(consensus_file):
    """
        Function to calculate sequence profiles

        Parameters
        ----------
        consensus_file : str
            path to consensus file (clustal omega fasta output)

        Return
        ----------
        pssm : pssm file
            # Hint check imports

    """

    pssm = None

    # Read the MSA file
    alignment = AlignIO.read(consensus_file, "fasta")
    
    # Generate Position Specific Scoring Matrix manually
    # since AlignInfo is deprecated
    pssm = []
    for i in range(alignment.get_alignment_length()):
        column = alignment[:, i]
        # Count occurrences of each character
        counts = {}
        for char in column:
            if char != 'X':  # chars_to_ignore
                counts[char] = counts.get(char, 0) + 1
        pssm.append(counts)

    return pssm


def sequence_logo_creator(sequence_profile_csv):
    """
        Function to read sequence profile csv file, plot sequence logo and saves as png

        Parameters
        ----------
        sequence_profile_csv : str
            path to sequence profile csv

        Return
        ----------
        None

    """

    # Hint: You can use pandas dataframe

    logo = None

    # TODO read csv file and create sequence logo
    # read data
    data = pd.read_csv(sequence_profile_csv)

    # create logo
    logo = logomaker.Logo(data
                          , color_scheme='chemistry',
                          figsize=(50, 5),
                          stack_order='small_on_top')

    logo.fig.savefig(SCRIPT_DIR / f"{OUTPUT_PREFIX}_sequence_logo.png")


def csv_writer(pssm, output_file):
    """
        Function to write probabilities to csv file

        Parameters
        ----------
        pssm : pssm file
            returned pssm from calculate_sequence_profiles

        output_file : str
            path for output file
            
        Return
        ----------
        None

    """
    # Collect all unique characters across all positions
    all_chars = set()
    for pos in pssm:
        all_chars.update(pos.keys())
    
    # a sorted header of the alphabet
    header = sorted(list(all_chars))
    
    # change the count to probability and fill missing positions with 0
    for _, l in enumerate(pssm, start=1):
        sum_init = sum(l.values())
        # Add missing characters with 0 count
        for char in header:
            if char not in l:
                l[char] = 0
        # Convert counts to probabilities
        for k in l.keys():
            l[k] = l[k] / sum_init if sum_init > 0 else 0

    # write the pssm to a csv file
    with open(output_file, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(pssm)

# Nothing to do here
if __name__ == "__main__":

    seq_profiles = calculate_sequence_profiles(sys.argv[1])
    # Example: seq_profiles = calculate_sequence_profiles("./msa_output.fasta")
    csv_writer(seq_profiles, SCRIPT_DIR / f"{OUTPUT_PREFIX}_sequence_profile.csv")
    sequence_logo_creator(SCRIPT_DIR / f"{OUTPUT_PREFIX}_sequence_profile.csv")
