
def countDigits(n):
    cnt = 0
    while n > 0:
        cnt+=1
        n = n // 10
    return cnt


def reverseNum(n):
    rev = 0
    while n > 0:
        r = n % 10
        rev = (rev * 10 ) + r
        n = n // 10
    
    return rev


def isPalindrom(n):
    num = n
    rev = 0
    while n > 0:
        r = n % 10
        rev = (rev * 10 ) + r
        n = n // 10
    print(rev,num)
    return rev == num


def armstrongNum(n):
    num = n
    res = 0
    while n > 0:
        r = n % 10
        res += pow(r, 3)
        n = n // 10
    return res == num

import math
def divisorCheck(n):
    sqrtN = int(math.sqrt(n))
    res = []
    for i in range(1, sqrtN+1):
        if n % i == 0:
            res.append(i )
            # Add the counterpart divisor
            # if it's different from i
            if i != n // i:
                # Add the counterpart
                # divisor to the list
                res.append(n // i) 
    
    return res
        

# Main function
if __name__ == "__main__":
    # N = 823
    # print("N:", N)
    # digits = countDigits(N)
    # print("Number of Digits in N:", digits)
    
    # revNum = reverseNum(N)
    # print("Reverse num", revNum)

    # palindrome = isPalindrom(343)
    # print("Palindrome", palindrome)
    
    # checkArmstrong = armstrongNum(153)
    # print("Armstring", checkArmstrong)
    
    result = divisorCheck(36)
    print("Divisible nums:", result)
                                
                            