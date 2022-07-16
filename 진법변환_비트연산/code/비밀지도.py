def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a1 = bin(arr1[i])[2:].zfill(n)
        a2 = bin(arr2[i])[2:].zfill(n)
        x = ''
        print(a1,a2)
        for idx in range(n):
            if a1[idx] == '1' or a2[idx] == '1':
                x += '#'
            elif a1[idx] == '0' and a2[idx] == '0':
                x += ' '
        answer.append(x)
    return answer