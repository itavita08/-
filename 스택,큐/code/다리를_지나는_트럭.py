from collections import deque

def solution(bridge_length, weight, truck_weight):
    time = 0
    deq_ln = [0]*bridge_length
    deq_tr = deque(truck_weight)
    while len(deq_ln):
        deq_ln.pop(0)
        time += 1
        if deq_tr:
            if deq_tr[0] + sum(deq_ln) <= weight:
                deq_ln.append(deq_tr.popleft())
            else:
                deq_ln.append(0)
    return time

bridge_length = 100
weight = 100
truck_weight = 	[10,10,10,10,10,10,10,10,10,10]

print(solution(bridge_length, weight, truck_weight))