def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    length = len(dna)
    return length

def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    return get_length(dna1) > get_length(dna2)



def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    return dna.count(nucleotide)




def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    return dna1.find(dna2) > 0
def  is_valid_sequence(dna):
    '''(str) - > Bool
    Return True if and only if the DNA sequence is valid
    (that is, it contains only nucleotide characters: 'A', 'T', 'C' and 'G').

    >>> is_valid_sequence('ATCGGTAAC')
    True
    >>> is_valid_sequence('ATCSGTAAC')
    False
    >>> is_valid_sequence('QWER')
    False
    >>> is_valid_sequence('AAAAAAA')
    True
    >>> is_valid_sequence('TTTTTT')
    True
    '''
    for c in dna:
        if  not((c =='A') or (c =='T') or (c =='C') or (c =='G')):
            return False
        
    return True
        




def  insert_sequence(dna1, dna2, pos):
    '''(str, str, int) - > str
    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.

    >>> insert_sequence('ATCGGTAAC', 'CC', 0)
    True
    >>> insert_sequence('ATCGGTAAC', 'CC', 1)
    False
    >>> insert_sequence('ATCGGTAAC', 'CC', 7)
    False
    >>> insert_sequence('AAA', 'CC', 3)
    True
    >>> insert_sequence('TTTTTT')
    True
    '''
    return dna1[:pos] + dna2 + dna1[pos:]

def get_complement(n):
    '''
    Return the nucleotide's complement.

    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G
    >>> get_complement('G')
    C
    '''
    if n == 'A':
        return 'T'
    elif n == 'T':
        return 'A'
    elif n == 'C':
        return 'G'
    elif n == 'G':
        return 'C'
    else:
        return False


def get_complement_sequence(dna):
    '''
    Return the nucleotide's complement.

    >>> get_complement_sequence('AT')
    TA
    >>> get_complement_sequence('CG')
    GC
    
    '''
    dna_complement = ''
    for c in dna:
        dna_complement += get_complement(c)
        
    return dna_complement
        
    
