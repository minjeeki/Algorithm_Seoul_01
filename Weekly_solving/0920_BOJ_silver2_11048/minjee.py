# DFS 코드 DP로 바꾸기 (이전 커밋과 비교해서 확인할 것)

import sys

sys.setrecursionlimit(10 ** 6)

def ft_dfs(cr, cc):


    # 이동 가능 범위
    dr = (1, 0, 1)
    dc = (0, 1, 1)
    # 종료 조건 : 마지막 위치에 도달하면 마지막 위치의 값을 반환한다
    if cr == (N - 1) and cc == (M - 1):
        return candies[cr][cc]
    # dp 활용하기 (이미 값을 저장한 경우라면 똑같은 재귀 안돌고 저장값 활용한다)
    if dp[cr][cc] != -1:
        return dp[cr][cc]
    # 방문처리가 필요하다면 -1에서 0으로 리셋한다 (0 아니고 candies[cr][cc]여도 됨)
    dp[cr][cc] = 0
    for i in range(3):
        nr = cr + dr[i]
        nc = cc + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            # dp 저장 : 현 위치에서 [N - 1][M - 1]까지 가면서 먹는 사탕의 최대 수
            dp[cr][cc] = max(dp[cr][cc], candies[cr][cc] + ft_dfs(nr, nc))
            # print('---', *dp, sep='\n')
    return dp[cr][cc]


N, M = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
max_candies = 0
ft_dfs(0, 0)
# print(*dp, sep='\n')
print(dp[0][0])


'''
탐색에서 DP로 바꾸기
1. dfs 함수에서 반환값을 설정한다, 반환값은 해당 위치의 dp값
2. 이미 방문한 것에 대해서는 재귀를 더 진행하지 않고 해당 값의 dp값을 반환한다.
3. 재귀 호출의 반환값을 dp의 해당 위치에 저장한다.

DFS에서는 사용하던 visited를 사용하지 않아도 되는 이유
DP는 이미 계산된 결과를 저장해두고 해당 위치에 다시 도달하면 재계산하지 않고 저장된 값을 사용한다.
따라서 동일한 좌표에 대해 여러번 방문하는 일은 발생하지 않는다.
특히 이 문제에서는 이동하는 경로가 위에서 아래, 왼쪽에서 오른쪽이기에 갔던 좌표를 다시 갈 일이 없다.
'''

# DFS 코드
# def ft_dfs(cr, cc, cur_candies):
#     global visited, max_candies

#     dr = (1, 0, 1)
#     dc = (0, 1, 1)
#     # 종료 조건
#     if cr == (N - 1) and cc == (M - 1):
#         max_candies = max(max_candies, cur_candies)
#         return
#     for i in range(3):
#         nr = cr + dr[i]
#         nc = cc + dc[i]
#         if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited:
#             visited.add((nr, nc))
#             ft_dfs(nr, nc, cur_candies + candies[nr][nc])
#             visited.remove((nr, nc))


# N, M = map(int, input().split())
# candies = [list(map(int, input().split())) for _ in range(N)]
# visited = set()
# visited.add((0, 0))
# max_candies = 0
# ft_dfs(0, 0, candies[0][0])
# print(max_candies)
