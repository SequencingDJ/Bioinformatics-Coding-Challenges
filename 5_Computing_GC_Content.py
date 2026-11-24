# create an empty dictionary
#with ai help
fasta_dict = {}

 # code below reads the supplied file, creates a dictionairy with its key being 'Rosalind_3452' etc and its associated sequence. 

with open("rosalind_GC.txt", "r") as file:
    current_key = None  
    for line in file:
        line = line.strip()  
        if line.startswith(">"):  
            current_key = line[1:] 
            fasta_dict[current_key] = {"sequence": "", "length": 0, "gc_content":0, "gc_percentage": 0,}  # Initialize correctly
            # the above basically creates the labels we would like to populate later on! important step.
        else:
            fasta_dict[current_key]["sequence"] += line  # Append sequence data
            fasta_dict[current_key]["length"] = len(fasta_dict[current_key]["sequence"])
            fasta_dict[current_key]["gc_content"] = (fasta_dict[current_key]["sequence"].count("G")+(fasta_dict[current_key]["sequence"].count("C")))
            fasta_dict[current_key]["gc_percentage"] = (fasta_dict[current_key]["gc_content"] / fasta_dict[current_key]["length"]) * 100


# Sort the dictionary by GC percentage in descending order
sorted_fasta = dict(sorted(fasta_dict.items(), key=lambda item: item[1]["gc_percentage"], reverse=True))
print(sorted_fasta)
