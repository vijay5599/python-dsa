# def subArrSum(nums, K):
#     N = len(nums)
#     res = []
#     for i in range(N):
#         sum = 0
#         for j in range(i, N):
#             sum += nums[j]
#             if sum == K:
#                 res.append(nums[i : j + 1])
#     return res


def subArrSum(nums, K):
    sum = 0
    sum_map = {0: [-1]}
    res = []

    for i in range(len(nums)):
        sum += nums[i]
        target = sum - K

        if target in sum_map:
            for j in sum_map[target]:
                res.append(nums[j + 1 : i + 1])
            print(res, "added")
        print(sum_map, i, "before")
        if sum in sum_map:
            sum_map[sum].append(i)
        else:
            sum_map[sum] = [i]
        print(sum_map, "after")
    return res


nums = [3, 1, 2, 4]
k = 6
print(subArrSum(nums, k))
# nums1 = [1, 2, 3]
# k1 = 3
# print(subArrSum(nums1, k1))
