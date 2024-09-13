n = int(input())
dp = [0] * (n + 1)  # dp 생성
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp[1] = 1   # dp[1]에 1 저장
    dp[2] = 2   # dp[2]에 2 저장
    for i in range(3, n + 1):   # dp[3]부터 dp[n]까지
        dp[i] = dp[i - 1] + dp[i - 2] # dp[i]값 구하는 점화식 생성
    answer = dp[n] % 10007  # 최종 정답
    print(answer)
