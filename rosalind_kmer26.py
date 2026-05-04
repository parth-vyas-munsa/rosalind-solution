'''
Given: A DNA string s
 in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s
.'''

from Bio import SeqIO
from itertools import product

# Step 1: Read FASTA file
record = SeqIO.read("rosalind_kmer.txt", "fasta")
sequence = str(record.seq)


bases = ['A', 'C', 'G', 'T']
kmers = [''.join(p) for p in product(bases, repeat=4)]


kmer_count = {kmer: 0 for kmer in kmers}


for i in range(len(sequence) - 3):
    kmer = sequence[i:i+4]
    if kmer in kmer_count:
        kmer_count[kmer] += 1


output = [str(kmer_count[k]) for k in kmers]
print(" ".join(output))

    
