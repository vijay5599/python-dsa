def frequency(nums):
    mp = {}
    for i in range(len(nums)):
        if nums[i] in mp:
            mp[nums[i]] += 1
        else:
            mp[nums[i]] = 1
    
    for x in mp:
        print(x, mp[x])

def highestFreq(nums):
    mp = {}
    for num in nums:
        mp[num] = mp.get(num, 0)+1
    
    print(mp)
    max_freq = 0
    max_element = nums[0]
    
    for num, freq in mp.items():
        if freq > max_freq:
            max_freq = freq
            max_element = num
    
    return max_element, max_freq

if __name__ == "__main__":
    
    # frequency([1, 2, 3, 1, 3, 5])
    element, count = highestFreq([1, 2, 3, 3, 1, 3, 5])
    print(element, count)
    # print