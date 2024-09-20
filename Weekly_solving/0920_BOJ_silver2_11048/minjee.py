# DFS (완전 탐색) 조건

def ft_dfs(cr, cc, cur_candies):
    global visited, max_candies

    # 이동 가능 범위
    dr = (1, 0, 1)
    dc = (0, 1, 1)
    # 종료 조건 (끝까지 도달 시 max값 업데이트)
    if cr == (N - 1) and cc == (M - 1):
        max_candies = max(max_candies, cur_candies)
        return
    # 다음에 이동할 위치 구하기
    for i in range(3):
        nr = cr + dr[i]
        nc = cc + dc[i]
        if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited:
            visited.add((nr, nc))
            ft_dfs(nr, nc, cur_candies + candies[nr][nc])
            visited.remove((nr, nc))
    return


N, M = map(int, input().split())
# 사탕 놓기
candies = [list(map(int, input().split())) for _ in range(N)]
# 방문 처리
visited = set()
visited.add((0, 0))
max_candies = 0
ft_dfs(0, 0, candies[0][0])
print(max_candies)