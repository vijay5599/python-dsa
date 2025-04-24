def appearOnce(nums):
    ## Method-1
    # mp = {}
    
    # for num in nums:
    #     mp[num] = mp.get(num, 0) + 1
    
    # for key, val in mp.items():
    #     if val == 1:
    #         return key
    
    
    # Method-2
    xorr = 0
    for num in nums:
        xorr ^= num
    return xorr

nums = [1, 1, 2, 2, 4, 3, 3]
print(appearOnce(nums))