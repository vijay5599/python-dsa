def twoSum(nums, target):
    mp = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in mp:
           return [mp[diff], i]
        mp[num] = i
    return None
   
nums = [2, 7, 4, 5]
target = 9
print(twoSum(nums, target)) 