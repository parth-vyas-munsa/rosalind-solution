'''
Given: An RNA string s
 of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s
.'''
from Bio import SeqIO
import math
for records in SeqIO.parse("rosalind_pmch.txt" , "fasta"):
    rna = records.seq


def secondry_str(str):
    n = str.count("A")
    print(n)
    m = str.count("C")
    print(m)

    n_fact = math.factorial(n)
    m_fact = math.factorial(m)

    return n_fact*m_fact

print(secondry_str(rna))

    