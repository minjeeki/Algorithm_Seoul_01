from collections import deque

n, m = map(int, input().split())
near_lst = [[] for _ in range(n + 1)]
kevin_lst = [0] * (n + 1)
kevin_lst[0] = 2147483649
for _ in range(m):
    a, b = map(int, input().split())
    near_lst[a].append(b)
    near_lst[b].append(a)

for i in range(1, n + 1):
    deq = deque()
    deq.append((i, 0))
    visited = set()
    visited.add(i)
    while deq:
        curnum = deq.popleft()
        kevin_lst[i] += curnum[1]
        for friend in near_lst[curnum[0]]:
            if friend not in visited:
                deq.append((friend, curnum[1] + 1))
                visited.add(friend)

min_kevin = min(kevin_lst)
result = kevin_lst.index(min_kevin)
print(result)