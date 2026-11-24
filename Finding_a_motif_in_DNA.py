with open("Rosalind/Week_3_June_1/rosalind_subs(2).txt", "r") as file:
    #lines 0 is dna, lines 1 is motif. as given in the .txt file.
    lines = [line.strip() for line in file.readlines()]
    DNA,motif = lines[0],lines[1]




def find_motifs(DNA , motif):
    """   # take in motif 
 Old method I don't really like. 
    """
    
    
    # store all positions in a list
    positions = []
    # define start
    start = 0
    
    # loop
    #originally wanted to do an index loop, 
    # but DNA.index will only give the FIRST occurance and stop there.

    while True:
        pos = DNA.find(motif,start)
        if pos == -1:
            break
        positions.append(pos+1)
        start = pos +1
    
    return print(*positions, sep=' ')


def find_motif_new(DNA, motif):
    """
    Find positions of a motif in DNA sequence, finds the first occurance. slices it and finds the next occurance.
    it then uses the offset (how much of the dna is already chopped off, )
     to adjust the position back to the original dna strand. 
    """
    collected_positions = []
    offset = 0  
    # Tracks how much has been sliced

    while len(DNA) >= len(motif):
        position = DNA.find(motif)
        if position == -1: 
        # only true when no matches
            break  
        # exit loop
        
        collected_positions.append(position + 1 + offset)  
        # Adjust position with total offset
        offset += position + 1  
        # Update offset to reflect slicing
        DNA = DNA[position + 1:]  
        # Slice DNA to continue searching

    return print(*collected_positions, sep=' ')


print(find_motif_new(DNA, motif))