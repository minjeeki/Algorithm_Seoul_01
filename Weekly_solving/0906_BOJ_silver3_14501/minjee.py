# 다음에 코드 풀 것임


'''DP : bottom-up'''
import sys
N = int(input())

# 사용자 입력 받기
schedule  = [list(map(int, input().split())) for i in range(N)]

dp = [0 for i in range(N + 1)]

for i in range(N):
    for j in range(i + schedult[i][0], N + 1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]
print(dp[-1])

'''
DP : top-down
뒤에서부터 접근 & 점화식 세우기
'''
N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    if i + li[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], li[i][1] + dp[i + li[i][0]])

print(dp[0])

'''
재귀
'''
N = int(input())
time_table = [list(map(int, input().split())) for _ in range(N)]

def solve(i):
    if i >= N:
        return 0
    ret = 0
    if i + time_table[i][0] <= N:
        ret = solve(i + time_table[i][0]) + time_table[i][1]
    ret = max(ret, solve(i + 1))
    return ret

print(solve(0))