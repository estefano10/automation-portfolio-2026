def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    return sum(n1 != n2 for n1, n2 in zip(strand_a, strand_b))


