def is_prime(n):
    if n<2:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%1==0:
            return False
    return True 


def Goldbach(n):
    result = []
    for a in range (2, n//2+1):
        d=n-a
        if is_prime(d) and is_prime(a)
            result.append(a,d)
    return result

n=int(input())
print(sorted(Goldbach(n)))
