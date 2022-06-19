# DFS,BFS
## 문제설명
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.    
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,    
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.   
## 입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.    
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.    
입력으로 주어지는 간선은 양방향이다.   
## 출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
## 예제
```
4 5 1  # N, M, V
1 2    # 정점의 번호
1 3
1 4
2 4
3 4
```
```
1 2 4 3
1 2 3 4
```
## 문제풀이
정점간의 방향이 없으므로 인접 행렬을 만들어 2차원 리스트를 만들어준다.   
BFS의 경우 for구문을 돌리면서 if문 조건에 해당하는 수들을 모두 queue에 담고 다음 for구문을 실행했지만   
DFS의 경우 for구문을 실행하고 if문 조건에 해당하는 수가 있을 경우 for구문을 종료하고 함수를 재 실행했다.   
## 코드
```python
from collections import deque

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for i in range(N+1)]   # 인접행렬 생성
visited = [0]*(N+1)                       

for i in range(M):   # 인접행렬 생성(방향이 상관없음)
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1
    
def dfs(V):  
    visited[V] = 1   # 방문한 곳 체크
    print(V,end=' ')
    for i in range(1,N+1):
        if (visited[i] == 0 and graph[V][i]) == 1:   # 전에 방문한 적이 없고 서로 연결되어있으면 다음 함수 실행
            dfs(i)
            
def bfs(V):
    queue = deque([V])   # queue 생성
    visited[V] = 0       # 방문한 곳 체크
    while queue:  # queue에 아무런 원소가 없으면 종료
        x = queue.popleft()   # queue[0] 가져오기
        print(x,end=' ')
        for i in range(1,N+1):
            if (visited[i] == 1 and graph[x][i]) == 1:  # 전에 방문한 적 없고 서로 연결되어있으면 다음 코드 실행
                queue.append(i)   # queue에 추가
                visited[i] = 0    # 방문한 곳 체크
                
dfs(V)
print()
bfs(V)
```
