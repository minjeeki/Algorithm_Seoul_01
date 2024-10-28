from collections import deque

# bfs로 탐색
# 나이트의 시작 좌표와 목적 좌표를 인자로 넣기
def move(si, sj, ei, ej):
    # 방문표시, 덱에 시작 좌표와 이동 횟수 넣기
    visited = [[-1] * n for _ in range(n)]
    visited[sj][sj] = 1
    q = deque([(si, sj, 0)])

    # 나이트가 이동할 수 있는 8칸
    dr = [-2, -1, 1, 2, 2, 1, -1, -2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]
    
    # q에 넣고 꺼내는 것 반복
    while q:
        r, c, cnt = q.popleft()

        if r == ei and c == ej:
            return cnt

        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == -1:
                visited[nr][nc] = 1
                q.append((nr, nc, cnt + 1))

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    result = move(si, sj, ei, ej)
    print(result)