# def rearrangeArray(nums):
#     pos = []
#     neg = []
    
#     for i in range(len(nums)):
#         if nums[i] < 0:
#             neg.append(nums[i])
#         else:
#             pos.append(nums[i])
        
#     print(pos, neg)    
#     for i in range(len(pos)):
#         nums[2*i] = pos[i]
#     for i in range(len(neg)):
#         nums[2*i+1] = neg[i]

#     return nums

# print(rearrangeArray([1, 1, -1, -2]))


def rearrangeArray(nums):
    n = len(nums)
    res = [0] * n
    pos, neg = 0, 1
    for num in nums:
        if num < 0:
            res[neg] = num
            neg+=2
        else:
            res[pos] = num
            pos+=2
    return res

print(rearrangeArray([1, 1, -1, -2]))