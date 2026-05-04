'''
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.'''


# List of probabilities for dominant phenotype per child
prob_dominant = [1, 1, 1, 0.75, 0.5, 0]

def expected_dominant_offspring(couples):
    """
    couples: list of 6 integers representing # of couples of each genotype type
    Returns expected number of dominant phenotype offspring
    """
    total = sum(c * 2 * p for c, p in zip(couples, prob_dominant))
    return total

if __name__ == "__main__":
    with open("rosalind_iev.txt", "r") as f:
        l = [float(i) for i in f.readline().strip().split(" ")]
    print(expected_dominant_offspring(l))

