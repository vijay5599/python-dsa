def loggestConsecutive(nums):

    if not nums:
        return 0
    num_set = set(nums)
    max_length = 1

    for num in num_set:
        # only check numbers that can be sequence starts
        if num - 1 not in num_set:
            curr_len = 1
            curr_num = num
            while curr_num + 1 in num_set:
                curr_len += 1
                curr_num += 1
            max_length = max(max_length, curr_len)

    return max_length


nums = [100, 200, 1, 3, 2, 4]
print(loggestConsecutive(nums))
nums1 = [3, 8, 5, 7, 6]
print(loggestConsecutive(nums1))
