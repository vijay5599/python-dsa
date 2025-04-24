def leftRotate(nums, k):
    l = 0
    r = len(nums)-1
    reverseArray(nums, l, k)
    reverseArray(nums, k+1, r)
    reverseArray(nums, l, r)
    
    return nums


def reverseArray(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1
    return nums

nums = [1, 2, 3, 4, 5, 6]
k = 2
res = leftRotate(nums, k)
print(res)