# 2156. 포도주 시식

import sys
input = sys.stdin.readline

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]

# DP 테이블 정의 및 초기값 지정
dp = [0] * (n + 1)
dp[1] = wine[1]
if n > 1:
    dp[2] = wine[1] + wine[2]

# 누적최댓값을 기록한 DP배열을 활용해 이전 3개 값 중
# 한 개를 선택하지 않는 경우의 수 중 최댓값을 DP배열 현재 값으로 업데이트
for i in range(3, n + 1):
    dp[i] = max(
        dp[i - 1],
        dp[i - 2] + wine[i],
        dp[i - 3] + wine[i - 1] + wine[i]
    )

print(dp[n])