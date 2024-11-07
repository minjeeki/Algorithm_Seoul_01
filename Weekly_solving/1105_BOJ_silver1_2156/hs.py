n = int(input())
grape = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

if n <= 2:
    print(sum(grape))

else:
    dp[1] = grape[1]
    dp[2] = grape[1] + grape[2]

    for i in range(3, n+1):
        # 각각 현재 포도주를 마시지 않는 경우, 이전 포도주를 마시지 않는 경우, 연속으로 두 잔을 마시는 경우
        dp[i] = max(dp[i-1], grape[i] + dp[i-2], grape[i] + grape[i-1] + dp[i-3])

    print(max(dp))

