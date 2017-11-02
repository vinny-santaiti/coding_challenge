def hamming_distance(v1, v2):
    """count of chars that are different"""
    v1 = list(v1)
    v2 = list(v2)
    if len(v1) != len(v2):
        return 0
    count = 0
    for index, char in enumerate(v1):
        if v1[index] != v2[index]:
            count += 1
    return count

assert hamming_distance([],[]) == 0
assert hamming_distance([0,1],[0,1]) == 0
assert hamming_distance("00","01") == 1
assert hamming_distance("karolin", "kathrin") == 3
assert hamming_distance("karolin", "kerstin") == 3
assert hamming_distance((1,0,1,1,1,0,1), (1,0,0,1,0,0,1)) == 2
assert hamming_distance("2173896", "2233796") == 3
