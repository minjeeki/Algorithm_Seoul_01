import sys
sys.setrecursionlimit(10 ** 6)

def dfs(i):
    if memo[i] != -1:
        return memo[i]
    
    if i == 0:
        return wine[0]
    elif i == 1:
        return wine[0] + wine[1]
    elif i == 2:
        return max(wine[0] + wine[2], wine[1] + wine[2], wine[0] + wine[1])

    memo[i] = max(dfs(i - 1), dfs(i - 2) + wine[i], dfs(i - 3) + wine[i - 1] + wine[i])
    return memo[i]

n = int(input())
wine = [int(input()) for _ in range(n)]

memo = [-1] * n

print(dfs(n - 1))