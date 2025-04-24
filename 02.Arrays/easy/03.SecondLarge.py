
def secondlarge(nums):
    large = float('-inf') 
    sec_large = float('-inf')
    
    for i in range(len(nums)):
        if nums[i] > large:
            sec_large = large
            large = nums[i]
        elif nums[i] > sec_large and nums[i] != large:
            sec_large = nums[i]
    
    return sec_large


if __name__ == "__main__":
    nums = [1,2,4,7,6,5]
    res = secondlarge(nums)
    print(res)