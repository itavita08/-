import sys
L = int(sys.stdin.readline())
input_data = list(sys.stdin.readline())    
M = 1234567891
r = 31
result =0

for i in range(L):
    result += (ord(input_data[i])-96)*(r**i)

print(result%M)    
 