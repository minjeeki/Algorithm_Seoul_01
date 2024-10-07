import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]    # 2차원 배열에 맞춘 dp 생성
    if n >2:    # 한줄의 스티커가 2개 이상일때
        dp[0][0] = arr[0][0]    # 본인
        dp[1][0] = arr[1][0]    # 본인
        dp[0][1] = dp[1][0] + arr[0][1] # 본인 + 대각선
        dp[1][1] = dp[0][0] + arr[1][1] # 본인 + 대각선
        for j in range(2, n):   # 2부터 n-1까지
            dp[0][j] = max(dp[1][j-2], dp[1][j-1]) + arr[0][j]  # 본인 + 바로 앞 대각선 or 본인 + 두칸 앞 대각선 중 큰 값
            dp[1][j] = max(dp[0][j-2], dp[0][j-1]) + arr[1][j]
        max_val = max(dp[0][n - 1], dp[1][n - 1])   # 마지막 열 둘 중 가장 큰 값
        print(max_val)

    elif n == 2:    # 한줄에 딱 두 개 있을 때
        max_val = max(arr[0][0] + arr[1][1], arr[1][0] + arr[0][1]) # 서로 대각선 값 합 중 큰 값
        print(max_val)
    else:   # 스티커가 각 줄에 하나씩만 있을 때
        print(max(arr[0][0], arr[1][0]))    # 둘 중 큰 값