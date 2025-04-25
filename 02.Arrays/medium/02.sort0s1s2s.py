# def sort0s1s2s(nums):
#     mp = {}
#     res = []
#     for num in nums:
#         mp[num] = mp.get(num, 0) + 1
    
#     for num in [0, 1, 2]:
#         freq = mp.get(num, 0)
#         res.extend(freq * [num])
#     return res

def sort0s1s2s(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low+=1
            mid+=1
        elif nums[mid] == 2:
            nums[high], nums[mid] = nums[mid], nums[high]
            high-=1
            mid+=1
        else:
            mid+=1  
    return nums

nums = [2,0,2,1,1,0]
p.rint(sort0s1s2s(nums))