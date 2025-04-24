
def printNum(i, n):
    if i > n: return
    print(i)
    return printNum(i + 1, n)

def printNumRev(i, n):
    if i < 1: return
    print(i)
    return printNumRev(i-1, n)
    
def naturalSum(i, sum):
    if i < 1:
        print(sum)
        return
    return naturalSum(i-1, sum + i)
    
def factorial(n):
    if n == 0 or n == 1: 
        return 1
    return n * factorial(n-1)

def revArray(nums, start, end):
    if start < end:
       nums[start], nums[end] = nums[end], nums[start]
       return revArray(nums, start+1, end-1)
       
def printArray(nums, n):
    for i in range(n):
        print(nums[i], end=" ")
    print()
    
def isPalindrome(s, l, r):
    if l >= r:
        return True
    while l < r and not s[l].isalnum():
        l+=1
    while l < r and not s[r].isalnum():
        r-=1
    if s[l].lower() != s[r].lower():
        return False
    return isPalindrome(s, l+1, r-1)

def fibonacci( n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    
def printFib(n):
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()

if __name__ == "__main__":
    # nums = printNum(1, 6)
    # print(nums) 
    
    # nums = printNumRev(6, 6)
    # print(nums) 
    
    # sum = naturalSum(4, 0)
    # print(sum) 

    # factorialNum = factorial(3)
    # print(factorialNum)
    
    # nums = [1, 2, 4, 5, 6]
    # start = 0
    # end = len(nums) 
    # printArray(nums, end)
    # revArray(nums, start, end-1)
    # printArray(nums, end)

    # test_cases = [
    #     "A man, a plan, a canal: Panama",
    #     "race a car",
    #     "AOCBA",
    #     "ABCBA"
    # ]
    # for s in test_cases:
    #     result = isPalindrome(s, 0, len(s) - 1)
    #     print(f"'{s}' is palindrome: {result}")
    n = 5
    # fibonacci(n)
    printFib(n)
