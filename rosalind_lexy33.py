'''
Given: A permutation of at most 12 symbols defining an ordered alphabet A
 and a positive integer n
 (n≤4
).

Return: All strings of length at most n
 formed from A
, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)'''


alphabet = input().split()
n = int(input())

with open("with.txt", "w", newline="\n") as f:
    
    def generate(s):
        if s:
            f.write(s + "\n")   
        
        if len(s) == n:
            return
        
        for ch in alphabet:
            generate(s + ch)

    generate("")



