'''
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
 is the string sc
 formed by reversing the symbols of s
, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s
 of length at most 1000 bp.

Return: The reverse complement sc
 of s
.'''

def revc_comp(string):
    strand = ""
    for i in string[::-1]:
        if i == "A":
            strand += "T"
        if i == "T":
            strand += "A"
        if i == "C":
            strand += "G"
        if i == "G":
            strand += "C"
    return strand


if __name__ == "__main__":
    with open("rosalind_dna.txt", "r") as f:
        string = f.readline().strip()
        strand = revc_comp(string)
        print(strand)