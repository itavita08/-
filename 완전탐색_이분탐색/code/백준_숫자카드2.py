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

# N = int(sys.stdin.readline())
# n = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# m = list(map(int, sys.stdin.readline().split()))
# answer = []


# for i in range(M):
#     count = 0
#     for j in range(N):
#         if n[j] == m[i]:
#             count += 1
#     answer.append(count)

# for i in answer:
#     print(i, " ", end='')    
