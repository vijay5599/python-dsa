# Subarray Sum Equals K - Solution Explanation

## Problem

Find all subarrays in an array that sum up to a given target K.

## Solution Approach

We use prefix sum technique with a hash map to find all subarrays with sum K in O(n) time complexity.

### Code

```python
def subArrSum(nums, K):
    sum = 0
    sum_map = {0: [-1]}  # Initialize with 0 sum at index -1
    res = []

    for i in range(len(nums)):
        sum += nums[i]
        target = sum - K

        if target in sum_map:
            for j in sum_map[target]:
                res.append(nums[j + 1 : i + 1])

        if sum in sum_map:
            sum_map[sum].append(i)
        else:
            sum_map[sum] = [i]
    return res
```

## Detailed Example

Let's walk through the algorithm with input: `nums = [3, 1, 2, 4]`, `k = 6`

### Initial State:

- sum_map = {0: [-1]}
- res = []

### Iteration 1: (i = 0, nums[0] = 3)

```
Current sum = 3
Target = 3 - 6 = -3
sum_map = {0: [-1], 3: [0]}
res = []
```

### Iteration 2: (i = 1, nums[1] = 1)

```
Current sum = 4
Target = 4 - 6 = -2
sum_map = {0: [-1], 3: [0], 4: [1]}
res = []
```

### Iteration 3: (i = 2, nums[2] = 2)

```
Current sum = 6
Target = 6 - 6 = 0
Found target in sum_map!
Add subarray nums[0:3] = [3,1,2]
sum_map = {0: [-1], 3: [0], 4: [1], 6: [2]}
res = [[3,1,2]]
```

### Iteration 4: (i = 3, nums[3] = 4)

```
Current sum = 10
Target = 10 - 6 = 4
Found target in sum_map!
Add subarray nums[2:4] = [2,4]
sum_map = {0: [-1], 3: [0], 4: [1], 6: [2], 10: [3]}
res = [[3,1,2], [2,4]]
```

## Time & Space Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Key Points

1. Use prefix sum to track running sum
2. Use hash map to store prefix sums and their indices
3. For each position, check if (prefix_sum - K) exists in map
4. If found, there's a subarray with sum K ending at current position

```

You can save this content in a file named `subarray_sum_explanation.md` in your project directory.
```
