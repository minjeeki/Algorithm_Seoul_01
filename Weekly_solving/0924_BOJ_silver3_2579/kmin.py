N = int(input())
lst = [int(input()) for _ in range(N)]  # 계단
dp = [0] * (N + 1)    # 빈 dp 생성
if N == 1:  # 계단 1개일때
    print(lst[0])
elif N == 2:    # 계단 2개 일때
    print(lst[0]+lst[1])
else:   # 계단 3개 이상일 때
    dp[1] = lst[0]  # dp[1]값 지정
    dp[2] = dp[1] + lst[1]  # dp[2]값 지정
    for i in range(3, N + 1):
        dp[i] = max(dp[i-3] + lst[i-1] + lst[i-2], dp[i-2] + lst[i-1])
        # lst의 0번인덱스가 dp의 1번 인덱스와 매칭되므로
    print(dp[-1])
