N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
n = N-1     # 찾아야 될 인덱스 값
m = M-1     # 찾아야 될 인덱스 값
dx = [-1, 0, -1]    # 역으로 찾아 나갈 거라 주어진 +는 -로 바꿔서 델타 작성
dy = [0, -1, -1]
dp[0][0] = lst[0][0]    # dp[0][0]은 고정
for j in range(1, M):   # 열 index가 0인 경우 위에거랑 합치면 된다
    dp[0][j] = lst[0][j] + dp[0][j-1]
for i in range(N):      # 행 index가 0인 경우 바로 옆에거랑 합치면 된다
    dp[i][0] = lst[i][0] + dp[i-1][0]
for i in range(1, N):   # index 1부터 ( 0은 이미 작성되어 있기 때문)
    for j in range(1, M):
        max_value = 0
        for k in range(3):  # 델타 적용
            value = lst[i][j]   # 본인 값
            nx = i + dx[k]  # 위에서 i, j의 범위를 1부터 N-1로 설정해놔서 따로 범위에 포함되는지 확인 안해도 된다
            ny = j + dy[k]
            value += dp[nx][ny]
            if value > max_value:   # 최종 최댓값이 dp[i][j]의 값이 된다
                max_value = value
        dp[i][j] = max_value
print(dp[n][m])