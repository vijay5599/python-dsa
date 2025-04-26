def leaderInArray(nums):
    res = [nums[len(nums)-1]]
    
    for i in range(len(nums)-2, -1, -1):
        if nums[i] > res[len(res)-1]:
            res.append(nums[i])
    
    return res[::-1]

nums = [10, 22, 12, 3, 0, 6]
print(leaderInArray(nums))
nums1 = [4, 7, 1, 0]
print(leaderInArray(nums1))


"""
Input: arr = [10, 22, 12, 3, 0, 6]
Output: 22 12 6
 
Input: arr = [4, 7, 1, 0]
Output: 7 1 0

"""