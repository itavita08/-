import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

max_v = -1e9
min_v = 1e9

def solution(i, arr):
    global add, sub, mul, div, max_v, min_v
    if i == n:                  # i가 입력한 수의 개수와 같아지면 최대값, 최솟값 비교
        max_v = max(max_v, arr)  
        min_v = min(min_v, arr)
    else:
        # 더하기
        if add > 0:
            add -= 1    # 더하기를 함으로 남아있는 더하기 개수 -1
            solution(i+1, arr + num[i])
            add += 1    # 원래대로 더하기 개수를 돌려논다
        # 빼기
        if sub > 0:
            sub -= 1
            solution(i+1, arr - num[i])
            sub += 1
        # 곱하기
        if mul > 0:
            mul -= 1
            solution(i+1, arr * num[i])
            mul += 1
        # 나누기
        if div > 0:
            div -= 1
            solution(i+1, int(arr / num[i]))
            div += 1
            
solution(1,num[0])
print(max_v)
print(min_v)

