from collections import deque
import sys

def solution():
    number = int(sys.stdin.readline())
    
    for i in range(number):
        que = deque()
        data = sys.stdin.readline().rstrip()
        for j in data:
            if j == "(":
                que.append(j)
            elif j == ")":
                if not que or que[-1] == ")":
                    que.append(j)
                    break
                else:
                    que.pop()
        print("YES" if not que else "NO")
                
            
solution()