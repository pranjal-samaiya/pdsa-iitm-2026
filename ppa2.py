def sortInRange(L, r):
    count = [0] * r

    # Count the occurrences of each number
    for x in L:
        count[x] += 1

    # Build the sorted list
    result = []
    for i in range(r):
        result.extend([i] * count[i])

    return result
