def dfs(cur_sum, weights_cnt):
    global max_sum

    if weights_cnt == 2:
        max_sum = max(max_sum, cur_sum)

    for idx in range(1, weights_cnt - 1):
        cur_get = weights[idx - 1] * weights[idx + 1]
        selected_value = weights.pop(idx)
        dfs(cur_sum + cur_get, weights_cnt - 1)
        weights.insert(idx, selected_value)

N = int(input())
weights = list(map(int, input().split()))
max_sum = 0
dfs(0, N)
print(max_sum)