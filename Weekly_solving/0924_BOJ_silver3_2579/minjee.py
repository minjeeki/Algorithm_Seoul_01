import sys
sys.setrecursionlimit(10000)

# DP를 적용한 DFS 함수
def ft_dfs(cur_idx, before_movement):
    # 마지막 계단에 도착한 경우, 그 계단의 점수를 반환
    if cur_idx == N - 1:
        dp[cur_idx][before_movement] = stairs[cur_idx]
        return stairs[cur_idx]

    # 이미 계산한 적이 있는 경우 DP 값을 반환
    if dp[cur_idx][before_movement] != -1:
        return dp[cur_idx][before_movement]

    max_total = 0

    # 직전 이동이 1칸 이동이었다면, 이번에는 2칸만 이동 가능
    if before_movement == 1 and cur_idx > 0:
        if cur_idx + 2 < N:
            max_total = max(max_total, ft_dfs(cur_idx + 2, 2) + stairs[cur_idx])
    else:
        # 1칸 이동 가능
        if cur_idx + 1 < N:
            max_total = max(max_total, ft_dfs(cur_idx + 1, 1) + stairs[cur_idx])
        # 2칸 이동 가능
        if cur_idx + 2 < N:
            max_total = max(max_total, ft_dfs(cur_idx + 2, 2) + stairs[cur_idx])
    
    # DP 테이블에 계산 결과 저장
    dp[cur_idx][before_movement] = max_total
    return max_total

# 입력 받기
N = int(input())
stairs = [int(input()) for _ in range(N)]

# DP 테이블 초기화: -1로 초기화하여 아직 계산되지 않았음을 표시
dp = [[-1 for _ in range(3)] for _ in range(N)]

# 첫 번째 계단부터 시작하여 DFS 탐색
if N == 1:
    print(stairs[0])
else:
    # 첫 번째 계단을 꼭 밟아야 한다는 조건이 없으므로, 두 번째 계단에서 시작할 수도 있음
    dp[0][1] = ft_dfs(0, 1)
    # print(dp)
    dp[1][2] = ft_dfs(1, 2)
    # print(dp)
    result = max(dp[0][1], dp[1][2])
    # print(dp)
    print(result)


# def ft_dfs(cur_idx, before_movement, total):
#     global max_total

#     if cur_idx == (N - 1):
#         max_total = max(max_total, total)
#         return
    
#     # cur_idx가 0이 아니고, before_movement가 1인 경우 : 무조건 2칸만 이동 가능
#     if before_movement == 1 and cur_idx > 0:
#         if cur_idx + 2 < N:
#             ft_dfs(cur_idx + 2, 2, total + stairs[cur_idx + 2])
#     else:
#         if cur_idx + 2 < N:
#             ft_dfs(cur_idx + 2, 2, total + stairs[cur_idx + 2])
#         if cur_idx + 1 < N:
#             ft_dfs(cur_idx + 1, 1, total + stairs[cur_idx + 1])

# N = int(input())
# stairs = [int(input()) for _ in range(N)]
# max_total = 0
# ft_dfs(-1, -1, 0)
# print(max_total)