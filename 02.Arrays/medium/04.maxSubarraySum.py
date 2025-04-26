def maxSubarraySum(nums):

    # max_sum = 0
    # for i in range(len(nums)-1):
    #     sum = 0
    #     for j in range(i, len(nums)-1): 
    #         sum += nums[j]
    #         max_sum = max(sum , max_sum)    
    # return max_sum
    
    max_sum = float('-inf')
    sum = 0
    for i in range(len(nums)-1):
        sum += nums[i]
        if sum > max_sum:
            max_sum = sum
        if sum <= 0:
            sum = 0
    return max_sum
nums = [-2,1,-3,4,-1,2,1,-5,4] 
print(maxSubarraySum(nums))