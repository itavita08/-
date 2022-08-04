from collections import deque

def solution(progresses,speeds):
    deq_pr = deque(progresses)
    deq_sp = deque(speeds)
    answer = []
    count = 0
    time = 0
    while deq_pr:
        if deq_pr[0] + (time*deq_sp[0]) >= 100:
            deq_pr.popleft()
            deq_sp.popleft()
            count += 1
        else:
            if count >= 1:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer   

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]        

print(solution(progresses, speeds))
 
