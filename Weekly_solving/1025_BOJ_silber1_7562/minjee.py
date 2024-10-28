from collections import deque

dx = (-1, -2, -2, -1, 1, 2, 2, 1)
dy = (-2, -1, 1, 2, -2, -1, 1, 2)

def ft_bfs(cx, cy, tx, ty):
    curdeq = deque()
    curdeq.append((cx, cy))
    visited = {(cx, cy)}
    nextdeq = deque()
    movement = 0
    while True:
        # 현재 movement에 해당하는 curdeq 값 한개씩 빼면서 진행
        while curdeq:
            px, py = curdeq.popleft()
            for i in range(8):
                nx = px + dx[i]
                ny = py + dy[i]
                if 0 <= nx < I and 0 <= ny < I and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    nextdeq.append((nx, ny))
                    if nx == tx and ny == ty:
                        return movement + 1
        # 빈 curdeq와 다음 movement값 들어있는 nextdeq 교환
        curdeq, nextdeq = nextdeq, curdeq
        movement += 1

T = int(input())
for _ in range(T):
    I = int(input())
    # cx, cy : 현재 나이트가 있는 칸
    cx, cy = map(int, input().split())
    # tx, ty : 나이트가 이동하려고 하는 칸
    tx, ty = map(int, input().split())
    # 상황에 따라 bfs 진행 여부 결정
    if cx == tx and cy == ty:
        print(0)
    else:
        print(ft_bfs(cx, cy, tx, ty))