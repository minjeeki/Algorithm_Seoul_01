# 16198. 에너지 모으기 (재귀, 백트래킹)

import sys
input = sys.stdin.readline

def recur(level, cnt):
    global max_v

    if level == N-2:
        max_v = max(max_v, cnt)
        return

    for i in range(1, len(arr)-1):
        temp = arr.pop(i)
        recur(level+1, cnt + arr[i-1] * arr[i])
        arr.insert(i, temp)     # 백트래킹

N = int(input())
arr = list(map(int, input().split()))
max_v = 0
recur(0, 0)
print(max_v)