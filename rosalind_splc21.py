'''
Given: A DNA string s
 (of length at most 1 kbp) and a collection of substrings of s
 acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s
. (Note: Only one solution will exist for the dataset provided.)'''


from Bio import SeqIO
from Bio.Seq import Seq

records = list(SeqIO.parse("rosalind_splc.txt", "fasta"))


dna_seq = records[0].seq

introns = [record.seq for record in records[1:]]



for intron in introns:
    dna_seq = dna_seq.replace(intron, "")


rna_seq = dna_seq.transcribe()

protein = rna_seq.translate(to_stop=True)

# Step 7: Print result
print(protein)