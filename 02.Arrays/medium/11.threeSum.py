def threeSum(nums):
    n = len(nums)
    nums.sort()
    res = []

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i+1
        k = n-1

        while(j < k):
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                res.append([nums[i] , nums[j] , nums[k]])
                while j < k and nums[j+1] == nums[j]:
                    j+=1
                while j < k and nums[k-1] == nums[k]:
                    k-=1
                j+=1
                k-=1
            elif sum < 0:
                j+=1
            else:
                k-=1
            
            
    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))





# ✅ Sort + Two Pointers
# - Sort the array first
# - Fix one element `nums[i]`, then use two pointers (`j`, `k`) to find two numbers such that: nums[i] + nums[j] + nums[k] === 0
# - If sum is less than 0 → move left pointer (j++)
# - If sum is more than 0 → move right pointer (k--)
# - Skip duplicates for both i, j, and k
# ⏱ Time: O(n^2), Space: O(1) (excluding result array)
