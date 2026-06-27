def is_prime(n):
    if n <2:
        return False
    for i in range (2,int (n**0.5)+1):
        if n % i == 0 :
            return False
    return True 
def twin_Prime(n,m):
    return [(nums,nums+2)for nums in range(n,m+1) if is_prime(nums) and is_prime(nums+2)]
