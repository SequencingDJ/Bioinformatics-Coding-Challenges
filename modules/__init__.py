def codon_to_protein_translation(sequence):
    """
    This function takes a supplied sequence, and converts it into a protein.

    Example use:
    >>>codon_to_protein_translation("GAAGAAGAAGAAGAAGAA")
    EEEEEE
    """

    # RNA codon table from stack overflow
    RNA_codon_table = {
    'A': ('GCU', 'GCC', 'GCA', 'GCG'),
    'C': ('UGU', 'UGC'),
    'D': ('GAU', 'GAC'),
    'E': ('GAA', 'GAG'),
    'F': ('UUU', 'UUC'),
    'G': ('GGU', 'GGC', 'GGA', 'GGG'),
    'H': ('CAU', 'CAC'),
    'I': ('AUU', 'AUC', 'AUA'),
    'K': ('AAA', 'AAG'),
    'L': ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'),
    'M': ('AUG',),
    'N': ('AAU', 'AAC'),
    'P': ('CCU', 'CCC', 'CCA', 'CCG'),
    'Q': ('CAA', 'CAG'),
    'R': ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
    'S': ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'),
    'T': ('ACU', 'ACC', 'ACA', 'ACG'),
    'V': ('GUU', 'GUC', 'GUA', 'GUG'),
    'W': ('UGG',),
    'Y': ('UAU', 'UAC'),}

    protein = []
    #break protein into triplets
    triplets = [sequence[i:i+3] for i in range(0,len(sequence), 3)]
    # to ensure all triplets are accounted for.
    for triplet in triplets:

        for key, codons in RNA_codon_table.items():
            if triplet in codons:
                protein.append(key)
                break
            #break ensures process stops once we FIND the relevant aa, without checking all the others.
                

    
    return "".join(protein)

