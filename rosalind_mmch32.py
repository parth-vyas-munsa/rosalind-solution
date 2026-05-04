'''
Given: An RNA string s
 of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s
.'''


from Bio.Seq import Seq
import math


s = "UCAUUACGAGAUUUCUGAACUUAAUUCUGACUUGCGAUGUUCUAAGUCCCAUGUAGGCGCAUAAGCCAAAAGCUCCCCGACUACGG"


rna = Seq(s)


A = rna.count("A")
U = rna.count("U")
C = rna.count("C")
G = rna.count("G")


au = math.factorial(max(A, U)) // math.factorial(abs(A - U))
cg = math.factorial(max(C, G)) // math.factorial(abs(C - G))

result = au * cg

print(result)