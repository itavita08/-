from collections import deque

card = int(input())
que = deque(i for i in range(1,card+1))
    
while(len(que)>1):  # 1장이 남을때 까지 반복
        que.popleft()  # 첫번째 카드를 빼고
        que.append(que.popleft())  # 그다음 카드는 맨뒤로 보내고

print(que[0])

