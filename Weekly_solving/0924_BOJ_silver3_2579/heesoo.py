n = int(input())
step = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

if n <= 2:
    print(sum(step))

else:
    dp[1] = step[1]
    dp[2] = step[1] + step[2]
    for i in range(3, n+1):
        # 각 계단에 도착했을 때 얻을 수 있는 점수의 최댓값 구하기 -> dp에 저장
        # 1칸 전에서 올라오는 경우 -> step[i]+step[i-1]+dp[i-3], 3계단 연속 밟는 것 방지
        # 2칸 전에서 올라오는 경우 -> step[i] + dp[i-2]
        dp[i] = max(step[i] + step[i-1] + dp[i-3], step[i]+dp[i-2])
    result = dp[n]
    print(result)