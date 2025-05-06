def maxProduct(nums):

    max_prod = 1
    for i in range(len(nums)):
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            max_prod = max(prod, max_prod)
    
    return max_prod

nums = [1,2,3,4,5,0]
print(maxProduct(nums))