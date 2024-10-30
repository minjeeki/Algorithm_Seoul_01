import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]  
answer = []
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)    # 서로 연결되어 있다
    lst[b].append(a)
def bfs(s): # bfs 정의
    visited = [-1] * (N+1)  # visited에 방문 표시뿐만 아니라 몇번 만에 방문하는지 최소 횟수도 적을 거야
    q = deque()
    q.append(s)
    visited[s] = 0  # 본인 visited 0으로 설정
    total_visit = 0 # 최종 결과
    while q:
        t = q.popleft()
        for w in lst[t]:
            if visited[w] == -1:    # 방문하지 않았다면
                q.append(w)
                visited[w] = visited[t] + 1 # 연결되어 있는 바로 전 visited값에 +=1
                total_visit += visited[w]   # 최종값에 값 추가
    return total_visit  # 최종값 반환

for i in range(1, N+1):
    answer.append((bfs(i), i))  # 몇번 째 사람인지 [1]인덱스에 넣어준다
answer.sort()   # [0]인덱스를 기준으로 동일한 값이 있을 경우 기존 순서대로 정렬(기존 순서가 번호가 낮은 사람부터 정렬되어 있음)
print(answer[0][-1])    # 맨 앞의 값의 [1]인덱스 출력



