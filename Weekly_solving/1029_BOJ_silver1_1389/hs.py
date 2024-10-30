from collections import deque

def bfs(node):
    visited = [0] * (n + 1)     # 방문여부 체크
    q = deque([(node, 0)])      # 노드와 케빈 거리를 전달할 덱
    visited[node] = 1           # 방문 처리
    check = [0] * (n + 1)       # 각 사람의 1번부터 n번 사람까지의 거리를 저장할 리스트

    while q:
        now, cnt = q.popleft()  # 현재 노드와 거리를 큐에서 꺼냄
        check[now] += cnt       # 거리를 누적해서 더하기

        for next in n_list[now]:
            if visited[next] == 0:
                visited[next] = 1
                q.append((next, cnt+1))

    return sum(check)           # n번 사람의 케빈 베이컨 수(기준 node에서 1번 ~ n번까지 거리의 합) 반환

n, m = map(int, input().split())
n_list = [[] for _ in range(n+1)]

for _ in range(m):              # 간선 정보를 입력 받아, 인접 리스트 구성
    v1, v2 = map(int, input().split())
    n_list[v1].append(v2)
    n_list[v2].append(v1)

num_list = [0] * (n+1)          # 각 사람의 케빈 베이컨 수를 저장할 리스트
for i in range(1, n+1):         # 1번 ~ n번 사람까지 각각 위 함수 호출하여 케빈 베이컨 수를 저장
    num_list[i] = bfs(i)

result = min(num_list[1:])      # 인덱스 0번은 0으로 제외하고, 1번부터 끝까지의 수 중 제일 작은 수 뽑기

for j in range(1, n+1):         # 케빈 베이컨 수가 같을 때는 번호가 작은 사람을 출력해야 함
    if num_list[j] == result:   # 앞부터 순차적으로 순회하다가, result 값과 같은 값이 나오면 바로 멈추기
        print(j)
        break