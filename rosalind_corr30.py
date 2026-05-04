'''
Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s
 in the dataset, one of the following applies:

s
 was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
s
 is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)'''

from Bio import SeqIO
from Bio.Seq import Seq
from collections import Counter

# Step 1: Read sequences
reads = []
for record in SeqIO.parse("rosalind_corr.txt", "fasta"):
    reads.append(str(record.seq))

# Step 2: Count reads and reverse complements
count = Counter(reads)

# include reverse complements
all_counts = Counter()
for read in reads:
    rc = str(Seq(read).reverse_complement())
    all_counts[read] += 1
    all_counts[rc] += 0  # ensure rc exists

# Step 3: Identify correct reads
correct = set()

for read in reads:
    rc = str(Seq(read).reverse_complement())
    if count[read] + count[rc] >= 2:
        correct.add(read)
        correct.add(rc)

# Step 4: Find incorrect reads
incorrect = []
for read in reads:
    rc = str(Seq(read).reverse_complement())
    if count[read] + count[rc] == 1:
        incorrect.append(read)

# Step 5: Hamming distance function
def hamming(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))

# Step 6: Find corrections
for bad in incorrect:
    for good in correct:
        if hamming(bad, good) == 1:
            print(f"{bad}->{good}")
            break





