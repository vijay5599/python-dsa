def majorityElement(nums):
    mp = {}
    n = len(nums)
    for num in nums:
        mp[num] = mp.get(num, 0) + 1
    
    for num, freq in mp.items():
        if freq > n//2:
            return num
    return None
    


nums = [4,4,2,4,3,4,4,3,2,4]
print(majorityElement(nums))