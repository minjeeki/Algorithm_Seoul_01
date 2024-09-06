N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [0] * (N+1) # 인덱스까지의 날짜의 최대 이익을 여기에 저장할 거야
for i in range(N): # 1일차부터 N-1일차까지
    for j in range(i+arr[i][0], N+1): # i일에 일을 했을 때 완료되는 날짜
        if dp[j] <dp[i] + arr[i][1]: # j일째까지 얻는 최대 이익이
            # i일째 얻는 최대이익 + i일에 시작해서 얻는 값보다 작으면
            #d[j] 바꿀거야
            dp[j] = dp[i] + arr[i][1]
print(dp[N])
