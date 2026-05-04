'''
Given: A DNA string s
 of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s
. Strings can be returned in any order.'''


from Bio import SeqIO
from Bio.Seq import Seq

def find_orfs_biopython(fasta_file):
    proteins = set()

    for record in SeqIO.parse(fasta_file, "fasta"):
        dna = record.seq

        # Check both strands
        for strand in [dna, dna.reverse_complement()]:
            
            # 3 reading frames
            for frame in range(3):
                seq = strand[frame:]
                
                # Translate sequence
                protein_seq = seq.translate(to_stop=False)
                
                # Split at stop codons
                for protein in str(protein_seq).split("*"):
                    
                    # Only keep sequences starting with M
                    for i in range(len(protein)):
                        if protein[i] == "M":
                            proteins.add(protein[i:])

    return proteins


# Example usage
fasta_file = "rosalind_orf (1).txt"

results = find_orfs_biopython(fasta_file)

for p in results:
    print(p)