
def secondSmall(nums):
    small = float('inf') 
    sec_Small = float('inf')
    
    for i in range(len(nums)):
        if nums[i] < small:
            sec_Small = small
            small = nums[i]
        elif nums[i] < sec_Small and nums[i] != small:
            sec_Small = nums[i]
    
    return sec_Small


if __name__ == "__main__":
    nums = [1,2,4,7,7,5]
    res = secondSmall(nums)
    print(res)