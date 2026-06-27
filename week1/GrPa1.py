# week 1 GrPa 1

# we are asked to create a program that takes a list of size L and a int that P
# we have to check what is the mininmun value of the difference of the max and min
# value of the subset of size P we can find in that list 




#first we define the function 

def find_min_Difference(L,P):

# the idea is to sort the list using .sort() inbuilt to create a ascending order list 

    L.sort()
    bracket_length = P
    list_size = L

#since sorted the biggest diff will be the max and min of the list 
    min_diff = max(L) - min(L)

# we run a for loop from the start to the end by creating a window of 5 elements 
    for i in range (list_size - bracket_length+1):
        if L(i+bracket_length-1)-L(i) < min_diff:
            min_diff = L(i+bracket_length-1)-L(i)
    return min_diff


L=eval(input().strip())
P=int(input())
print(find_min_Difference(L,P))
