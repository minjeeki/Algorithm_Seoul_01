import sys
input = sys.stdin.readline
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = triangle[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + triangle[i][0]  # 각행의 0번 인덱스는 바로 위의 0번 인덱스 dp와 더해지면 된다
    dp[i][i] = dp[i-1][i-1] + triangle[i][i]    # 마찬가지로 -1번 인덱스도 바로 위의 -1번 인덱스 dp와 더하면 된다
if n >=2:   # n이 2이상이면
    for i in range(2, n):
        for j in range(1, i):   # 여기 범위 잘못 지정(i-1로)해서 틀림
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])   # 바로 위 행의 연결되어 있는 값 둘 중 큰 값을 더한다
    result = max(dp[n-1])
    print(result)
else:   # n이 2미만이면
    result = max(dp[n-1])
    print(result)