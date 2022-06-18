# DFS
- Depth First Search, 깊이 우선 탐색
- 하나의 경우의 수에 대하여 모든 경우의 수를 조사하고 다음 경우의 수를 조사
![DFS](https://user-images.githubusercontent.com/105635205/174428575-9135010c-eee2-46a6-a7f2-842317d8cdb9.png)
## DFS(깊이우선탐색) 구현
- 미로 찾기
```python
while len(stack)>0:  # 스택 데이터 여부
  now = stack.pop()  # 스택의 가장 마지막 데이터 추출
  if now == dest:    # 정답여부 검사
    return True
  x = now[1]
  y = now[0]
  if x -1 > -1:      # 왼쪽으로 이동할 수 있으면 스택에 추가하고 방문여부 표시 
    if maps[y][x-1] == 1:
      stack.append([y,x-1])
      maps[y][x-1]=2
  if x +1 < hori:    # 오른쪽으로 이동할 수 있으면 스택에 추가하고 방문여부 표시
    if maps[y][x+1] == 1:
      stack.append([y,x+1])
      maps[y][x+1]=2
  if y -1 > -1:      # 위로 이동할 수 있으면 스택에 추가하고 방문여부 표시
    if maps[y-1][x] == 1:
      stack.append([y-1,x])
      maps[y-1][x]=2
  if y +1 < verti:   # 아래로 이동할 수 있으면 스택에 추가하고 방문여부 표시
    if maps[y+1][x] == 1:
      stack.append([y+1,x])
      maps[y+1][x]=2
return False
```
# BFS
- Breadth First Search, 넓이 우선 탐색
- 하나의 경우의 수에 대한 다음 단계의 모든 경우의 수를 조사하면서 해를 찾는 과정
![BFS](https://user-images.githubusercontent.com/105635205/174430231-143858d7-907f-458d-84aa-6ba611192e4e.png)
## BFS(넓이우선탐색) 구현
- 최단경로찾기
```python
while len(queue)>0:     # queue 데이터 존재
  count = len(queue)    # 같은거리에 있는 queue 데이터 개수
  for time in range(count):   # 같은 거리에 있는 queue 개수 만큼 검사
    now = queue.pop()         
    if now == dest:           # 정답이면 반환
      return answer
    for i in data:            # 방문하지 않은 연결된 길이라면 queue에 추가하고 방문표시
      if i[0]==now and visited[i[1]-1]==False:
        queue.append(i[1])
        visited[i[1]-1]=True
      elif i[1]==now and visited[i[0]-1]==False:
        queue.append(i[0])
        visited[i[0]-1]=True
  answer += 1                # 거리를 1 더 벌린다
return answer
```
