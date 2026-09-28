dna_sequence = "ATGCGTATCGGATCGATTACG"


sequence_length = len(dna_sequence)


nucleotide_counts = {"A": 0, "T": 0, "G": 0, "C": 0}

valid_bases = ["A", "T", "G", "C"]


for x in dna_sequence:
    if x not in valid_bases:
        print("the sequence caontain not valid nucleotide", x)
        break
    else:
        nucleotide_counts[x] += 1



index = 0
while index < 4:
    nucleotide = valid_bases[index]
    print(nucleotide, ":", nucleotide_counts[nucleotide])
    index += 1



def calculate_gc_content(sequence):
    GC_percent = ((sequence.count("G") + sequence.count("C")) / len(sequence)) * 100
    return GC_percent



GC_percent = calculate_gc_content(dna_sequence)
print(GC_percent)