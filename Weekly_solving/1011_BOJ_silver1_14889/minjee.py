# 스타트 팀의 능력치와 링크 팀의 능력치의 차이 최소화
def ft_backtracking(idx, cnt_team_l, cnt_team_s, sum_team_l, sum_team_s):
    global min_gap
    # 기저 조건 : 전체 팀 배정 완료 시
    if idx == N:
        tuple_l = tuple(team_l)
        if tuple_l not in made_set:
            made_set.add(tuple_l)
            made_set.add(tuple(team_s))
            min_gap = min(min_gap, abs(sum_team_l - sum_team_s))
        return
    # 재귀
    if cnt_team_l < N // 2:
        rel_sum = 0
        for item in team_l:
            rel_sum += (powers[item][idx] + powers[idx][item])
        team_l.append(idx)
        ft_backtracking(idx + 1, cnt_team_l + 1, cnt_team_s, sum_team_l + rel_sum, sum_team_s)
        team_l.pop()
    if cnt_team_s < N // 2:
        rel_sum = 0
        for item in team_s:
            rel_sum += (powers[item][idx] + powers[idx][item])
        team_s.append(idx)
        ft_backtracking(idx + 1, cnt_team_l, cnt_team_s + 1, sum_team_l, sum_team_s + rel_sum)
        team_s.pop()

N = int(input())
powers = [list(map(int, input().split())) for _ in range(N)]
total = 0
min_gap = 100 * N * N
made_set = set()
team_l = []
team_s = []
ft_backtracking(0, 0, 0, 0, 0)
print(min_gap)