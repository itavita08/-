
def func(a):
    if a == 0:
        return '0'
    elif a==1:
        return '1'
    if a%2 ==1:
        return func(a//2) + '1'
    elif a%2 ==0:
        return func(a//2) + '0'
a = int(input())
i = func(a)
print(i)
