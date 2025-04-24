def longestSubArrWithSum(nums, N, K):
    max_length =0
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += nums[j]
            if sum == K:
                max_length = max(j - i + 1, max_length)
                
    return max_length
    



nums = [2, 3, 5, 1, 4]
print(longestSubArrWithSum(nums, N=len(nums), K=10))