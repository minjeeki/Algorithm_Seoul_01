# ------------- queue를 사용하는 BFS 기본 코드 ------------- #
# 0. 시작 노드를 큐에 넣는다.
#    visited 배열에 시작 노드를 방문 표시한다.
# 1. 큐가 비어있지 않은 동안 다음을 반복한다:
#    1.1 큐에서 노드를 꺼낸다.
#    1.2 꺼낸 노드의 모든 인접 노드를 확인한다.
#    1.3 인접 노드 중 방문하지 않은 노드를 큐에 넣고 **방문 표시**한다. (중요)
# 2. 모든 노드를 탐색할 때까지 위 과정을 반복한다.

# ------------- 아래 함수 부분 다음주 시험! ------------- #
from collections import deque

def bfs():
    while q:
        node = q.popleft()
        for neighbor in arr[node]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True
# ------------- 여기까지 ------------- #

# 아래는 입력 예시 (안써도 됨)
V, E = map(int, input().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)
visited = [False] * len(V)

q = deque()
q.append(1)
visited[1] = True
bfs()



# ------------- 2차원 배열의 경우 ------------- #
# 2차원 배열의 경우, graph는 n x m 크기의 배열로 설정
# visited 역시 같은 크기의 2차원 배열로 설정

from collections import deque

def bfs():
    while q:
        x, y = q.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = x + di, y + dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = True

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

q = deque()
q.append((0, 0))
visited[0][0] = True
bfs(0, 0)