


# # PS: Given an integer N, print the following pattern : 
# # Examples:
# # Input Format: N = 3
# # Result: 
# # * 
# # * * 
# # * * *


# def printTriangle(n):
#     for i in range(n):
#         for j in range(i+1):
#             print("*", end=" ")
#         print()

# printTriangle(6)


# # Input Format: N = 3
# # Result: 
# # * * *
# # * * 
# # *

# def printReverseTriangle(n):
#     for i in range(n, 0, -1):
#         for j in range(i):
#             print("*", end=" ")
#         print()

# printReverseTriangle(6)



# # Problem Statement: Given an integer N, print the following pattern : 
# # Input Format: N = 3
# # Result: 
# # 1
# # 1 2 
# # 1 2 3


# def numTriangle(n):
#     for i in range(1, n+1):
#         for j in range(1, i):
#             print(j, end=" ")
#         print()
    
# numTriangle(5)

# def numReverseTriangle(n):
#     for i in range(n, 1, -1):
#         for j in range(1, i):
#             print(j, end=" ")
#         print()

# numReverseTriangle(6)



# def tringle(n):
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ", end=" ")
#         for j in range(2 * i - 1):
#             print("*", end=" ")
#         for j in range(n-i-1):
#             print(" ", end=" ")
#         print()

# tringle(6)

# def reverseTringle(n):
#     for i in range(n):
#         for j in range(i):
#             print(" ", end=" ")
#         for j in range(2 * n -(2 * i + 1)):
#             print("*", end=" ")
#         for j in range(i):
#             print(" ", end=" ")
#         print()

# reverseTringle(5)



# def rectanle(n):
#     for i in range(n):
#         for j in range(n):
#             if i == 0 or i == n-1 or j == 0 or j == n-1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()

# rectanle(6)
# # * * * * * *
# # *         *
# # *         *
# # *         *
# # *         *
# # * * * * * *