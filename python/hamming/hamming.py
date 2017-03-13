def distance(first, second):
    if len(first) != len(second):
        raise ValueError

    hamming = 0        

    for i in range(0, len(first)):
        if first[i] != second[i]:
            hamming += 1

    return hamming