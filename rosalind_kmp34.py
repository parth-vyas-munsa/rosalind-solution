'''
Given: A DNA string s
 (of length at most 100 kbp) in FASTA format.

Return: The failure array of s
.'''

from Bio import SeqIO   


record = next(SeqIO.parse("munnu.txt", "fasta"))
s = str(record.seq)


failure = [0] * len(s)
print(failure)


# j = 0


# for i in range(1, len(s)):
    
    
#     while j > 0 and s[i] != s[j]:
#         j = failure[j - 1]
    
    
#     if s[i] == s[j]:
#         j += 1
    
    
#     failure[i] = j


# print(*failure)