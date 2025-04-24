
def maxConsecOnes(nums):
    max_count = 0
    count =0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)
    return max_count

nums = [1, 1, 0, 1, 1, 1]
print(maxConsecOnes(nums))