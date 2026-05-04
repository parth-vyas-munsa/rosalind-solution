'''
Given: An RNA string s
 having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.

Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s
, modulo 1,000,000.'''

MOD = 1_000_000

def count_matchings(s):
    n = len(s)
    memo = {}

    
    def is_pair(a, b):
        return (a == 'A' and b == 'U') or \
               (a == 'U' and b == 'A') or \
               (a == 'C' and b == 'G') or \
               (a == 'G' and b == 'C')

    def dp(i, j):
        
        if i > j:
            return 1
        
        if (i, j) in memo:
            return memo[(i, j)]

        total = 0

        
        for k in range(i + 1, j + 1, 2):  
            if is_pair(s[i], s[k]):
                left = dp(i + 1, k - 1)
                right = dp(k + 1, j)
                total += left * right
                total %= MOD

        memo[(i, j)] = total
        return total

    return dp(0, n - 1)



rna = "AGACUAUAGAGGUACUACAUUAUAUUCGAAUGUAUACUAAUUAGGCGCCUGGCCGUACACCGGUUAUUAUAAGGAUCGAUCCGCCUGCAGGUAACGCUAGACCGGUAUUAUAAUUAUGCUAUGCACGCCGCUGUACGCUCUACGGAGCAGUACUUGAUCAGCAGGCCUGGCGCCUACGAUGCGUCAUGGGCCUAGAUUACGAUCACGUGUACGCAGCGAUUAUACUAAUCCGCAUGGGACGCGUCGCAUAUGCGCCCCUUAAGUAGUA"
print(count_matchings(rna))