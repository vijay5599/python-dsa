def unionArray(num1, num2):
    mp = {}
    for i in range(len(num1)):
        mp[num1[i]] = mp.get(num1[i], 0)+1
        
    for j in range(len(num2)):
        mp[num2[j]] = mp.get(num2[j], 0)+1
        
    return list(mp.keys())

num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [2,3,4,4,5,11,12]
res = unionArray(num1, num2)
print(res)