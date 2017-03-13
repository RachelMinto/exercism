import re

def to_rna(dna):
    dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    if re.search('[^GCTA]', dna):
        return ''

    dna_nucleotides = list(dna)
    rna_nucleotides = map(lambda x: dna_to_rna[x], dna_nucleotides)
    return ''.join(rna_nucleotides)