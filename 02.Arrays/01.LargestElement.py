import math
def largestElement(nums):
    max = nums[0]
    for i in range(0, len(nums)):
        if nums[i] > max:
            max = nums[i]
    
    return max

# if __name__ == "__main__":
nums = [1, 2, 6, 4, 5]
large = largestElement(nums)
print(large)