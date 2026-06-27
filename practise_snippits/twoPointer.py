
def two_sum(nums: list[int] , target: int ) -> list[int]:
    left, right = 0 , len(nums )-1
    while left < right :
        s = nums [left]+nums[right]
        if s == target: 
            return [left,right]
        elif s<target : left+= 1

        else:right -=1
    return [-1,-1]

        
# check if the sum of 2 no is == target 
# we will take 2 pointers and run them from start and end and if the a+b
# is equal to the target then we return the a and b and if it is smaller then target then we move the a ++
# if it is greater then the target then we move b__

