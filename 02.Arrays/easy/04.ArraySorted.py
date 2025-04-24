def arraySorted(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            return False
    return True
    

nums = [1, 5, 3, 4, 5]
res = arraySorted(nums)
print(res)