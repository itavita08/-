def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = participant[-1]
    for idx,i in enumerate(completion):
        if participant[idx] != i:
            answer = participant[idx]
            break
    return answer