def solution(answers):
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    answer1=[]
    answer2=[]
    answer3=[]
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(answers)):
        i1 = i%5
        answer1.append(a1[i1])
        i2 = i%8
        answer2.append(a2[i2])
        i3 = i%10
        answer3.append(a3[i3])
    for i in range(len(answers)):
        if answer1[i] == answers[i]:
            count1 += 1
        if answer2[i] == answers[i]:
            count2 += 1
        if answer3[i] == answers[i]:
            count3 += 1
    if count1 > count2 and count1 > count3:
        return [1]
    elif count3 > count2 and count3 > count1:
        return [3]
    elif count2 > count1 and count2 > count3:
        return [2]
    elif count1 == count2 and count1 > count3:
        return [1,2] 
    elif count1 == count3 and count1 > count2:
        return [1,3]     
    elif count3 == count2 and count3 > count1:
        return [2,3]     
    elif count1 == count2 and count1 == count3:
        return [1,2,3]