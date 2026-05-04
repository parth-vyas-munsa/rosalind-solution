'''
Given: Two positive integers k
 (k≤7
) and N
 (N≤2k
). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N
 Aa Bb organisms will belong to the k
-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.'''


import math

def probability_at_least_N(k, N):
    n = 2 ** k          # total organisms
    p = 0.25            # probability of Aa Bb
    
    prob = 0.0
    
    for i in range(N, n + 1):
        comb = math.comb(n, i)   # n choose i
        prob += comb * (p ** i) * ((1 - p) ** (n - i))
    
    return prob

# Example:
k = 7
N = 34
result = probability_at_least_N(k, N)

print(round(result, 3))