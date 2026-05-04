'''
Given: A positive integer n≤7
.

Return: The total number of permutations of length n
, followed by a list of all such permutations (in any order).'''

import math
import itertools


num = int(input())
print(math.factorial(num))

perm = itertools.permutations(range(1, num+1))
for p in perm:
    print(*p)