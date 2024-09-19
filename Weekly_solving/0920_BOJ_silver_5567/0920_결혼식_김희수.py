from collections import deque

def wedding(node):          # 덱 이용한 BFS
    visited = [0]*(v+1)     # 방문표시 리스트
    visited[node] = 1       # 함수로 넘긴 노드의 방문표시
    q = deque([node])       # 덱에 해당 노드 넣기

    while q:                # q에 숫자가 있는 동안 계속 반복
        now = q.popleft()   # 덱에서 숫자 꺼내기

        if now == 1 or now in n_list[1]:    # 친구의 친구까지만 초대해야 함
            for next in n_list[now]:        # node = 1(본인) 이거나, 1의 인접 노드인 경우만 고려하기 위한 조건
                if visited[next] == 0:      # 위 조건으로 1의 인접 노드들의 인접 노드까지만 방문 가능
                    visited[next] = 1
                    q.append(next)

    return visited

v = int(input())    # v -> 노드의 수
e = int(input())    # e -> 간선의 수

n_list = [[] for _ in range(v+1)]       # 간선 정보 저장할 리스트

for _ in range(e):                      # 간선 정보 저장하기
    v1, v2 = map(int, input().split())
    n_list[v1].append(v2)
    n_list[v2].append(v1)

result = sum(wedding(1)) - 1    # 방문하여 1로 바꾼 노드만 결혼식에 참석, 1을 빼는 이유는 결혼 당사자인 1번 노드가 방문 표시 되었기 때문
print(result)