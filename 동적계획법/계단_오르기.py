# n = int(input())
# score =[0]
# for _ in range(n):
#     score.append(int(input()))
# result = [0]*(n+1)

# def fib(n):
#     if n == 1:
#         print(score[1])
#     else:
#         result[1] = score[1]
#         result[2] = score[1] + score[2]
#         for i in range(3,n+1):
#             result[i] = max(score[i]+score[i-1]+result[i-3],score[i]+result[i-2])
#         return print(result[-1])
    
# fib(n)
result = [0]
result.append(1)
print(result)

        
        
    


