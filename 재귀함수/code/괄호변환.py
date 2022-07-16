

def solution(p):
    if correct(p) == True:
        return p
    elif len(p) == False:
        return ''
    else:
        return func(p)

def uvc(p):
    count1 = 0
    count2 = 0
    for i in range(len(p)):
        if p[i] == "(":
            count1 += 1
        else:
            count2 += 1
        if count1 == count2:
            u = p[:i+1]
            if (i + 1)== len(p):
                v = ''
            else:
                v = p[i+1:]
            break
    return u, v

def correct(p):
    stack = []
    for i in p:
        if i =='(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] == '(':
                stack.pop()
    if len(stack) != 0:
        return False
    else:
        return True

def func(p):
    result = ''
    answer = ''
    print(p)
    if not len(p): 
        return ""
    u,v = uvc(p)
    if correct(u) == True:
        result = u + func(v) 
    else:
        answer += '('
        answer += func(v)
        answer += ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        result += answer
    return result

p = "()))((()"
solution(p)
