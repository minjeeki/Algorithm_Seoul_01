
from collections import deque

N = int(input()) # 상근이의 동기 수
M = int(input()) # 관계 수
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0]*(N+1) # 0 ~ N까지 인덱스 만들어 주기
count = 0

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def BFS(x):
    q = deque([x])
    visited[x] = 1
    
    while q:
        friend = q.popleft()
        for people in graph[friend]:
            if visited[people] == 0:
                q.append(people)
                visited[people] = visited[friend] + 1

BFS(1)
for idx in range(2, N+1): # 1부터 시작하는 데 1은 상근이라 셀 필요 x
    if 0< visited[idx] <=3:
        count += 1

print(count)