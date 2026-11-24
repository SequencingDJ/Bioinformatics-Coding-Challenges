
from Bio import SeqIO

def read_fasta_sequences(file_path):
    # Load all sequences as strings
    return [str(record.seq) for record in SeqIO.parse(file_path, "fasta")]

def longest_common_substring_multiple(sequences):
    if not sequences:
        return ""

    shortest = min(sequences, key=len)
    longest = ""

    for i in range(len(shortest)):
        for j in range(i + 1, len(shortest) + 1):
            candidate = shortest[i:j]
            if all(candidate in seq for seq in sequences):
                if len(candidate) > len(longest):
                    longest = candidate
    return longest



print(read_fasta_sequences("rosalind_lcsm.txt"))