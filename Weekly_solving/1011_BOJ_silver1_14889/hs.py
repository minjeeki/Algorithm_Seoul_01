
n = int(input())
soccer = [list(map(int, input().split())) for _ in range(n)]
player = []
result = []
visited = [0] * n
minnum = float('inf')


def divide(start, level):
    global minnum
    
    # 3. n//2명을 다 뽑았다면, visited 방문표시를 통해 팀을 나눌 수 있음
    # 4. for문으로 i, j가 모두 방문표시 된 경우, 모든 쌍의 능력치 합을 구할 수 있음
    # 5. 동일하게 i, j가 모두 방문표시 되지 않은 경우의 능력치 합도 구할 수 있음
    # 6. minnum을 무한대 값으로 설정하고, 팀의 능력치 차이를 도출할 때마다 값을 비교해서 최소인 값 도출
    if level == n // 2:
        team_a = 0
        team_b = 0
        for i in range(n):
            for j in range(n):
                if visited[i] == 1 and visited[j] == 1:
                    team_a += soccer[i][j]

                elif visited[i] == 0 and visited[j] == 0:
                    team_b += soccer[i][j]
        minnum = min(minnum, abs(team_a - team_b))
        return

    # 1. 주어진 n명의 플레이어 중 n//2명을 뽑는 모든 경우의 수
    # 2. player라는 빈 리스트에 n//2를 뽑아서 넣기
    # - 조건 : 중복 x, i에서 하나씩 증가시키며 다음 재귀함수 호출 (그래야 경우의 수 중복이 발생하지 않음)
    # - visited 방문표시 : n//2명을 다 뽑았을 때마다 팀을 나누어 계산하기 위함
    for i in range(start, n):
        if i not in player:
            player.append(i)
            visited[i] = 1
            divide(i+1, level+1)
            player.pop()
            visited[i] = 0


divide(0, 0)
print(minnum)
