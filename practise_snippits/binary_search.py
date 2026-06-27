def binarysearch(L,v):
    low = 0
    high = len(L)-1
    while low<= high:
        mid  = low + high //2
        if L[mid] <v:
            low = low +1
        elif L[mid]>v:
            high = mid -1
        else:
            return mid
    return False


L = [1,2,3,4,5,7,67,88,99]
print(binarysearch (L,88))
