# gc_content.py

from Bio import SeqIO

def calculate_gc_content(sequence):
    """
    Calculate GC content for a given DNA sequence.
    Args:
        sequence (str): DNA sequence
    Returns:
        float: GC content percentage
    """
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

def gc_content_sliding_window(sequence, window_size):
    """
    Calculate GC content using a sliding window approach.
    Args:
        sequence (str): DNA sequence
        window_size (int): Size of the sliding window
    Returns:
        list of float: GC content percentages for each window
    """
    gc_contents = []
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i + window_size]
        gc_contents.append(calculate_gc_content(window))
    return gc_contents

def parse_sequences(file_path):
    """
    Parse sequences from a FASTA or FASTQ file.
    Args:
        file_path (str): Path to the FASTA or FASTQ file
    Returns:
        list of str: List of sequences
    """
    sequences = []
    with open(file_path, "r") as handle:
        for record in SeqIO.parse(handle, "fasta" if file_path.endswith(".fasta") else "fastq"):
            sequences.append(str(record.seq))
    return sequences
