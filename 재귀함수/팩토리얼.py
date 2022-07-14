n = int(input())
def factory(n):
    if n == 0:
        return 1 
    return n*factory(n-1)

print(factory(n))