import sys
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO

def calculate_consensus_sequence(clustal_omega_file):

    """
        Function to calculate consensus sequence

        Parameters
        ----------
        clustal_omega_file : str
            path to clustal omega output file

        Return
        ----------
        None

    """

    consensus = None

    # Calculate consensus sequence and print out
    # Since there is 1 alignment in the file, we can use AlignIO.read
    # Clustal Omega typically produces a single alignment
    alignment = AlignIO.read(clustal_omega_file, "fasta")
    
    # Get consensus using modern BioPython API
    # Use simple majority voting for each position
    consensus_str = ""
    for i in range(alignment.get_alignment_length()):
        column = alignment[:, i]
        # Count occurrences of each character
        counts = {}
        for char in column:
            if char != '-':  # Ignore gaps
                counts[char] = counts.get(char, 0) + 1
        
        # Get most common character (or 'X' if all gaps)
        if counts:
            consensus_str += max(counts, key=counts.get)
        else:
            consensus_str += 'X'
    
    consensus = consensus_str
    print(consensus)


if __name__ == "__main__":
    calculate_consensus_sequence(sys.argv[1])
    # Example: calculate_consensus_sequence("./msa_output.fasta")

