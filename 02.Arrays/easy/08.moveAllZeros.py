def moveAllZeros(nums):
    # Initialize pointer for non-zero elements
    nonZeroIndex = 0
    
    # Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nonZeroIndex] = nums[i]
            nonZeroIndex += 1
    
    print(nums)
    # Fill remaining positions with zeros
    while nonZeroIndex < len(nums):
        nums[nonZeroIndex] = 0
        nonZeroIndex += 1
    
    return nums

# Test case
nums = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
res = moveAllZeros(nums)
print(res)