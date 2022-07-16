import sys

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

while True:
    num = sys.stdin.readline().strip()  
    if int(num) == 0:
        break
    result = 0
    for idx,i in enumerate(reversed(num)):
        n = idx + 1
        result += int(i)*factorial(n)
    print(result)
    
