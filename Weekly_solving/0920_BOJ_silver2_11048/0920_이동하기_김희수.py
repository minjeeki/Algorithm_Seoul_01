# dfs로 탐색하며 max값 갱신하기 -> stack 이용
# 각 좌표의 max값은 candy 라는 2차원 리스트에 저장
# 답은 맞게 나오지만 시간초과

# def candy_maze(i, j):
#     stack = []
#     stack.append((i, j))
#     candy[i][j] = maze[i][j]
#
#     while stack:
#         r, c = stack.pop()
#
#         for k in range(3):
#             nr = r + dr[k]
#             nc = c + dc[k]
#             if 0 <= nr < n and 0 <= nc < m:
#                 candy[nr][nc] = max(candy[r][c] + maze[nr][nc], candy[nr][nc])
#                 stack.append([nr, nc])
#
#
# n, m = map(int, input().split())
# maze = [list(map(int, input().split())) for _ in range(n)]
# candy = [[0] * (m) for _ in range(n)]
#
# dr = [0, 1, 1]  # 이동할 수 있는 왼쪽, 대각선, 아래 방향
# dc = [1, 1, 0]
#
# candy_maze(0, 0)
# result = candy[n - 1][m - 1]
# print(result)

# -----------------------------------------------------------------

# dp로 풀기

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
candy = [[0] * (m) for _ in range(n)]

candy[0][0] = maze[0][0]

for i in range(n):
    for j in range(m):
        if i > 0:
            candy[i][j] = max(candy[i][j], candy[i-1][j] + maze[i][j])      # 위에서 아래로 내려오며 max 갱신
        if j > 0:
            candy[i][j] = max(candy[i][j], candy[i][j-1]+maze[i][j])        # 왼쪽에서 오른쪽으로 가며 max 갱신
        if i > 0 and j > 0:
            candy[i][j] = max(candy[i][j], candy[i-1][j-1] + maze[i][j])    # 대각선 방향으로 내려가며 max 갱신

result = candy[n-1][m-1]
print(result)