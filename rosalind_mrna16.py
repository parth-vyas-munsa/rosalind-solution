'''
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)'''


def count_rna_strings(protein):
    MOD = 1000000

    codon_count = {
        'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2,
        'W': 1, 'P': 4, 'H': 2, 'Q': 2, 'R': 6,
        'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2,
        'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4
    }

    result = 1

    for aa in protein:
        result = (result * codon_count[aa]) % MOD

    # multiply by stop codons
    result = (result * 3) % MOD

    return result


with open ("" , 'r') as f:
 protein = f.readline()
print(count_rna_strings(protein))