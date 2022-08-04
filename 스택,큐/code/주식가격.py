from collections import deque

def solution(prices):
    answer = []
    que = deque(prices)
    while que:
        delete = que.popleft()
        count = 0
        for i in que:
            if delete <= i:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    return answer

prices = [1, 2, 3, 2, 3]

print(solution(prices))
