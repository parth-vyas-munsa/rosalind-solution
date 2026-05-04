'''
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.'''


def reverse_complement(s):
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(comp[c] for c in reversed(s))



def find_reverse_palindromes(dna):
    results = []
    n = len(dna)
    
    for i in range(n):
        for l in range(4, 13):
            if i + l <= n:
                substring = dna[i:i+l]
                if substring == reverse_complement(substring):
                    results.append((i+1, l)) 
                    
    return results



from Bio import SeqIO
for records in SeqIO.parse("rosalind_revp.txt" , "fasta"):
    dna = records.seq


results = find_reverse_palindromes(dna)


for pos, length in results:
    print(pos, length)