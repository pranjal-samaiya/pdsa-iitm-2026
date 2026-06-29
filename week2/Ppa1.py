def binarySearchIndexAndComparisons(L, k):
    left = 0
    right = len(L) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if L[mid] == k:
            return (True, comparisons)
        elif L[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return (False, comparisons)
