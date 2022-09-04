from itertools import permutations
def solution(numbers):
    n = list(numbers)
    a = []
    answer = []
    for i in range(1,len(numbers)+1):
        a.extend(permutations(n,i))    
    a2 = [int(''.join(j)) for j in a]
    for x in a2:
        if x < 2:
            continue
        check = True
        for y in range(2,int(x**0.5)+1):
                if x % y == 0:
                    check = False
                    break
        if check ==True:
            answer.append(x)
    return len(set(answer))
