'''
Given: Positive integers n
 and k
 such that 100≥n>0
 and 10≥k>0
.

Return: The total number of partial permutations P(n,k)
, modulo 1,000,000.'''

mod = 1000000

def permutation(n, k):
    result = 1
    for i in range(k):
        result = (result * (n - i)) % mod
    return result

print(permutation(94, 10))