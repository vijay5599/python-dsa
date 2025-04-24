
def missingNum(nums, N):
    nSum = (N * (N+1)) // 2
    
    sum = 0
    for i in range(len(nums)):
        sum +=  nums[i]
    print(sum , nSum)
    return nSum - sum
    
    



nums = [1, 2, 4, 5]
res = missingNum(nums, 5)
print(res)