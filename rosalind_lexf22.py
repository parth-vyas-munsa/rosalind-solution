'''
Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n
 (n≤10
).

Return: All strings of length n
 that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).'''


from itertools import product


with open ("rosalind_lexf.txt" , "r") as f :
 alphabet = f.readline().strip().split(",")

 c = " ".join(alphabet)
 print(c)
 

 
 alphabet.sort()
 n = 3


all_strings = product(alphabet, repeat=n)


all_strings = [''.join(tup) for tup in all_strings]


for s in all_strings:
    print(s)