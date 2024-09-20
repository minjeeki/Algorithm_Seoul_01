def ft_dfs(num, chonsu):
    global visited

    # 가지치기 (상근이의 친구의 친구만, 친구의 친구의 친구는 안돼)
    if chonsu >= 2:
        return
    # 범위 내 모든 친구 샤라웃
    for next_num in near_lst[num]:
        # print(num, next_num)
        visited.add(next_num)
        ft_dfs(next_num, chonsu + 1)

N = int(input())
M = int(input())
# 인접 리스트 만들기
near_lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    near_lst[a].append(b)
    near_lst[b].append(a)

# 상근이는 1번
sangun = 1
visited = set()
visited.add(sangun)
ft_dfs(sangun, 0)
# print(*list(visited))
# 상근이 제외 초대하는 동기 수
print(len(visited) - 1)