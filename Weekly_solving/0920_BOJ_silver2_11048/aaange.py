# N: 행의 수, M: 열의 수를 입력받음
N, M = map(int, input().split())

# 데이터를 저장할 리스트 초기화
data = []

# dp 배열 초기화: N x M 크기의 2차원 리스트
# dp[i][j]는 (0, 0)에서 (i, j)까지의 최댓값을 저장
dp = [[0 for c in range(M)] for r in range(N)]

# 각 행의 데이터를 입력받아 data 리스트에 추가
for i in range(N):
    data.append(list(map(int, input().split())))

# 시작점 (0, 0)의 값을 dp 배열에 초기화
dp[0][0] = data[0][0]

# dp 배열을 채우기 위한 이중 반복문
for i in range(0, N):
    for j in range(0, M):
        # (i, j)에서 오른쪽 아래 대각선으로 이동할 경우
        if i + 1 < N and j + 1 < M:
            # (i, j)에서 (i+1, j+1)로 이동할 때의 최댓값 업데이트
            dp[i + 1][j + 1] = max(dp[i][j] + data[i + 1][j + 1], dp[i + 1][j + 1])

        # (i, j)에서 아래로 이동할 경우
        if i + 1 < N:
            # (i, j)에서 (i+1, j)로 이동할 때의 최댓값 업데이트
            dp[i + 1][j] = max(dp[i][j] + data[i + 1][j], dp[i + 1][j])

        # (i, j)에서 오른쪽으로 이동할 경우
        if j + 1 < M:
            # (i, j)에서 (i, j+1)로 이동할 때의 최댓값 업데이트
            dp[i][j + 1] = max(dp[i][j] + data[i][j + 1], dp[i][j + 1])

# 최종적으로 (N-1, M-1)까지의 최댓값을 출력
print(dp[N - 1][M - 1])
