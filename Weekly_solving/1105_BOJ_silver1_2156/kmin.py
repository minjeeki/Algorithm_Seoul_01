import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)   # 한줄 한줄 입력 받아 arr에 어펜드
if n == 1:
    print(arr[0])   # 1일 때
elif n == 2:
    print(arr[0] + arr[1])  # 2일 때
else:   # 3이상일 때
    dp = [0] * (n + 1)
    dp[1] = arr[0]  # 굳이 dp1부터 시작안하고 dp0부터 arr과 인덱스 맞춰서 만드는게 더 나은 거 같음
    dp[2] = arr[0] + arr[1]
    for i in range(3, n + 1):
        dp[i] = max(dp[i-3] + arr[i-2] + arr[i-1], dp[i-1], dp[i-2] + arr[i-1]) # 최댓값은 3가지 경우 중 하나
    print(dp[-1])   # 마지막 인덱스 dp출력