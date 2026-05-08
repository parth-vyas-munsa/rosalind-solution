'''
Given: An RNA string s
 of length at most 300 bp.

Return: The total number of noncrossing matchings of basepair edges in the bonding graph of s
, modulo 1,000,000.'''

def count_matchings(rna):

    
    pairs = {
        'A': 'U',
        'U': 'A',
        'C': 'G',
        'G': 'C'
    }

    
    def solve(seq):

        
        
        if len(seq) <= 1:
            return 1

        
        total = solve(seq[1:])

        
        for i in range(1, len(seq)):

            
            if pairs[seq[0]] == seq[i]:

                
                left = seq[1:i]

                
                right = seq[i+1:]

            
                total += solve(left) * solve(right)

        return total

    return solve(rna) % 1000000


rna = "ACUGCAGGGCUGGAGACUGGCGUUUGGGGAAGGGUAAUUUA"

print(count_matchings(rna))