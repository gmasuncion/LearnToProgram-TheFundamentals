def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    dna_length = len(dna)

    return dna_length


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    
    for char in dna:
        if nucleotide == char:
            count = count + 1
    
    return count
    


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    check = dna2 in dna1
    
    return check


def is_valid_sequence(dna):
    """ (str) -> bool
    
    Return True if and only if the DNA sequence is valid, meaning only 
    characters 'A', 'T', 'C', and 'G' are included in dna. 
    
    >>> is_valid_sequence('ATCG')
    True
    >>> is_valid_sequence('BBB')
    FALSE
    
    """
    valid = True
    
    for char in dna:
        if (char not in 'ATCG'):
            valid = False
    
    return valid


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
    
    Return the concatenation of dna2 into dna1 at a given position in dna1, 
    index
    
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
     >>> insert_sequence('CGCGCC', 'CAT', 1)
    'CCATGCGCC'
    
    """
    
    if is_valid_sequence(dna1) == True and is_valid_sequence(dna2) == True:
        new_dna = dna1[ : index] + dna2 + dna1[index: ]
    else: 
            return 'Please insert a valid DNA'    
    
    return new_dna

def get_complement(nuc):
    for char in nuc:
        if(nuc == 'A'):
            return 'T'
        elif(nuc == 'T'):
            return 'A'
        elif(nuc == 'C'):
            return 'G'
        elif(nuc == 'G'):
            return 'C'
        else:
            return None        

def get_complementary_sequence(dna):
    """ (str) -> str
    
    Return the DNA sequence that is complementary to the given DNA sequence.
    
    >>> get_complementary_sequence('AT')
    'TA'
    
    """
    
    new_dna = ''
    for char in dna:
        new_dna = new_dna + get_complement(char)
            
    return new_dna
