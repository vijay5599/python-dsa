
def reverseArray(nums, l, r):
    print(l, r)
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1
    return nums

nums = [1, 2, 3, 4, 5]
l = 0
r = len(nums)-1
res = reverseArray(nums, l, r)
print(res)