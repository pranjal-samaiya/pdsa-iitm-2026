def selectionSort(L):
    n = len(L)
    if n <1:
        return(L)
    for i in range (n):
        minpos = i 
        for j in range (i+1,n):
            if L[j]<L[minpos]:
                minpos =j
        (L[i],L[minpos]) = (L[minpos],L[i])
    return(L)

L = [324,23,423,4,234,2,3423,23]
print(selectionSort(L))
