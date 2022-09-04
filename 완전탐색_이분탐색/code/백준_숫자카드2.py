import sys

N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
nums = {}
for i in n:
    if i not in nums:
        nums[i] = 1
    else:
        nums[i] += 1
        
M = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
for i in m:
    if i in nums:
        print(nums[i], "", end="")
    else:
        print(0, "", end="")

# N = 10
# n = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
# M = 8
# m = [10, 9, -5, 2, 3, 4, 5, -10]
# answer = []


# for i in range(M):
#     count = 0
#     for j in range(N):
#         if n[j] == m[i]:
#             count += 1
#     answer.append(count)

# for i in answer:
#     print(i, " ", end='')    
