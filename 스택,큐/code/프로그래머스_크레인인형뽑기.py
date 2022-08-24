from collections import deque

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    moves = deque(moves)
    buckets = []
    cnt = 0

    while moves:
        move = moves.popleft()
        for i in range(len(board)):
            doll = board[i][move-1]
            if doll != 0:
                board[i][move-1] = 0
                if buckets and buckets[-1] == doll:
                    buckets.pop()
                    cnt += 2
                else:
                    buckets.append(doll)
                break
    return cnt

print(solution(board, moves))

def solution2(board, moves):
    que = deque()
    count = 0
    
    for i in moves:
        for j in range(len(board)):
            catch = board[j][i-1]
            if catch != 0:
                board[j][i-1] = 0
                if que and que[-1] == catch:
                    que.pop()
                    count += 2
                else:
                    que.append(catch)
                break
    return count

print(solution2(board, moves))