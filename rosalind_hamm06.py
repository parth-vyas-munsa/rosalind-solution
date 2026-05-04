'''
Given two strings s
 and t
 of equal length, the Hamming distance between s
 and t
, denoted dH(s,t)
, is the number of corresponding symbols that differ in s
 and t
. See Figure 2.

Given: Two DNA strings s
 and t
 of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)
.'''
def hamm(s, t):
    count = 0
    assert len(s) == len(t)
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    return count

with open ("rosalind_hamm.txt" , 'r') as f:
    s = f.readline().strip()
    
    t = f.readline().strip()
print(hamm(s,t))