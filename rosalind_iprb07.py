'''
Given: Three positive integers k
, M
, and n
, representing a population containing k+m+n
 organisms: k
 individuals are homozygous dominant for a factor, m
 are heterozygous, and n
 are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''

def dominant(k,m,n):
    T = k + m + n
    ##AA mate with  three
    # probabilities of each pairing
    p_AA_AA = (k * (k - 1)) / (T * (T - 1))
    p_AA_Aa = (k * m) / (T * (T - 1))
    p_AA_aa = (k * n) / (T * (T - 1))

    p_Aa_AA = (m * k) / (T * (T - 1))
    p_Aa_Aa = (m * (m - 1)) / (T * (T - 1))
    p_Aa_aa = (m * n) / (T * (T - 1))

    p_aa_AA = (n * k) / (T * (T - 1))
    p_aa_Aa = (n * m) / (T * (T - 1))
    p_aa_aa = (n * (n - 1)) / (T * (T - 1))

    # multiply by dominant probability
    p_dominant = (
        p_AA_AA * 1 +
        p_AA_Aa * 1 +
        p_AA_aa * 1 +
        p_Aa_AA * 1 +
        p_Aa_Aa * 0.75 +
        p_Aa_aa * 0.5 +
        p_aa_AA * 1 +
        p_aa_Aa * 0.5 +
        p_aa_aa * 0
    )

    return p_dominant


print(round(dominant(26,19,25) , 5))
