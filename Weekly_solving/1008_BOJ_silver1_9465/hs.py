#Testcase 수
T = int(input())
#Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*n for _ in range(2)]  # 최댓값 저장할 dp 리스트

    if n == 1:                      # 열이 하나인 경우 위, 아래 스티커의 값 중 더 큰 값을 출력
        print(max(arr[0][0], arr[1][0]))
        continue

    dp[0][0] = arr[0][0]        # 첫 번째 열과 두 번째 열의 경우는 dp값 지정하고 시작
    dp[1][0] = arr[1][0]
    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]

    for j in range(2, n):               # 세 번째 열부터 마지막 열까지 dp 리스트에 최댓값 저장하기
        # 현재 스티커 위치로 올 수 있는 이전 위치 중 최댓값 구하기
        dp[0][j] = max(dp[1][j-1], dp[1][j-2], dp[0][j-2]) + arr[0][j]  # 첫 번째 행의 j번째 열에 대해 최댓값 계산
        dp[1][j] = max(dp[0][j-1], dp[0][j-2], dp[1][j-2]) + arr[1][j]  # 두 번째 행의 j번째 열에 대해 최댓값 계산

    print(max(dp[0][n-1], dp[1][n-1]))  # 1번 행, 2번 행의 마지막 열 중 더 큰 값이 최대 점수