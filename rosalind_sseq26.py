'''
Given: Two DNA strings s
 and t
 (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s
 in which the symbols of t
 appear as a subsequence of s
. If multiple solutions exist, you may return any one.'''




from Bio import SeqIO

def find_subsequence_indices(fasta_file):
    # Read the two sequences
    records = list(SeqIO.parse(fasta_file, "fasta"))
    
    s = str(records[0].seq)  # main sequence
    t = str(records[1].seq)  # subsequence to find

    indices = []
    j = 0  # pointer for t

    # Traverse s to find t as subsequence
    for i in range(len(s)):
        if j < len(t) and s[i] == t[j]:
            indices.append(i + 1)  # 1-based indexing
            j += 1

    # Check if full subsequence was found
    if j == len(t):
        return indices
    else:
        return None


# Run
result = find_subsequence_indices("rosalind_sseq (1).txt")

if result:
    print(" ".join(map(str, result)))
else:
    print("Subsequence not found")