from collections import deque

def solution(priorities, location):
    que = deque([(i,j) for i,j in enumerate(priorities)])  # location과의 비교를 위해
    answer = 0
    while True:
        printer = que.popleft()
        if any(printer[1] < q[1] for q in que):  # any를 사용해 다음 대기들보다 하나라도 우선순위가 낮으면
            que.append(printer)
        else:
            answer += 1     # 출력되는 순서
            if printer[0] == location:
                return answer