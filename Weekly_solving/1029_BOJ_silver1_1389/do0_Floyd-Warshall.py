# 1389. 케빈 베이컨의 6단계 법칙 (Floyd-Warshall)

import sys
input = sys.stdin.readline
INF = int(1e7)

N, M = map(int, input().split())
# 2차원 행렬 graph
graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

# 플로이드 워셜 알고리즘 사용
for k in range(1, N+1): # 모든 중간 정점 k
    for i in range(1, N+1):
        for j in range(1, N+1):
            # i -> k (모든 k값) -> j 로 가는 최단 거리 갱신
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = int(1e9)
result = 0
for i in range(1, N+1):
    total = sum(graph[i][1:])
    if ans > total:
        ans = total
        result = i
print(result)