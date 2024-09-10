def ft_backtracking(spot, depth, total_muscle):

    # 현재 값에 대한 상태 반영
    visited[spot] = True
    now_total_muscle = total_muscle + A_lst[spot] - K
    # 가지치기 조건
    if now_total_muscle < 500:
        return
    # 기저 조건
    if depth >= N:
        global cnt_routine
        cnt_routine += 1
        return
    # 다음 순서 정하기
    for idx_next in range(N):
        if visited[idx_next] == False:
            ft_backtracking(idx_next, depth + 1, now_total_muscle)
            visited[idx_next] = False



N, K = map(int, input().split())
A_lst = list(map(int, input().split()))
visited = [False] * N
cnt_routine = 0
for idx_ex1 in range(N):
    ft_backtracking(idx_ex1, 1, 500)
    visited[idx_ex1] = False

print(cnt_routine)