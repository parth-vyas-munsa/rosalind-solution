'''
Given: A collection of k
 (k≤100
) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)'''


from Bio import SeqIO

def read_fasta(filename):
    return [str(record.seq) for record in SeqIO.parse(filename, "fasta")]

def longest_common_substring(sequences):
    shortest = min(sequences, key=len)
    n = len(shortest)
    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            substr = shortest[start:start+length]
            if all(substr in seq for seq in sequences):
                return substr
    return ""

if __name__ == "__main__":
    sequences = read_fasta("rosalind_lcsm (1).txt")  
    result = longest_common_substring(sequences)
    print(result)