'''
Given: A positive integer n≤6
.

Return: The total number of signed permutations of length n
, followed by a list of all such permutations (you may list the signed permutations in any order).'''


import itertools

n = 3
numbers = list(range(1, n+1))

total = 0

for perm in itertools.permutations(numbers):
    for signs in itertools.product([1, -1], repeat=n):
        
        total += 1
        
        signed_perm = [perm[i] * signs[i] for i in range(n)]
        
        print(*signed_perm)

print(total)


