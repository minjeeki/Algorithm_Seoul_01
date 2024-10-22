# 델타 탐색
# 네 방향 탐색하며 인접한 사탕이 색이 다르다면 색을 바꾸기
# 행, 열 탐색해서 연속한 사탕의 수 구하기

# 오답이유
# - 조건문 들여쓰기 ....
def find(arr):

    max_candy = 0       # 최대 연속 사탕 개수를 저장할 변수

    for i in range(n):  # 가로 방향으로 연속된 사탕 탐색
        stack = []      # 현재 연속된 사탕을 저장할 스택
        for j in range(n):
            # 스택이 비어있거나 이전 사탕과 같은 색상이면 스택에 추가
            if len(stack) == 0 or stack[-1] == arr[i][j]:
                stack.append(arr[i][j])
            else:                       # 이전 사탕과 다른 색상이면
                if len(stack) > 1:      # 현재까지의 연속 사탕 개수와 max_candy 비교하여 더 큰 값 저장
                    max_candy = max(max_candy, len(stack))
                stack = [arr[i][j]]     # 새로운 색상의 사탕으로 스택 초기화
        if len(stack) > 1:              # 해당 열의 탐색이 끝났을 때, 스택이 비어있지 않으면 연속된 사탕이 있다는 것
            max_candy = max(max_candy, len(stack))  # 기존 max_candy 값과, 현재 탐색한 연속된 사탕의 수 중 더 큰값으로 갱신

    for j in range(n):  # 세로 방향도 위와 똑같이 탐색
        stack = []
        for i in range(n):
            if len(stack) == 0 or stack[-1] == arr[i][j]:
                stack.append(arr[i][j])
            else:
                if len(stack) > 1:
                    max_candy = max(max_candy, len(stack))
                stack = [arr[i][j]]
        if len(stack) > 1:
            max_candy = max(max_candy, len(stack))

    return max_candy

n = int(input())
candy = [list(input().strip()) for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

result = 0
for r in range(n):
    for c in range(n):
        for k in range(4):
            # 델타 탐색
            nr = r + dr[k]
            nc = c + dc[k]

            # 인접한 사탕이 현재 칸과 다른 사탕일 때만 함수 실행
            # 1. 함수 실행 전, 현재 칸과 함수 실행 할 인접 칸의 사탕 교환
            # 2. 함수 실행
            # 3. 원래 상태로 복구
            if 0 <= nr < n and 0 <= nc < n:
                if candy[r][c] != candy[nr][nc]:
                    candy[r][c], candy[nr][nc] = candy[nr][nc], candy[r][c]
                    result = max(result, find(candy))
                    candy[nr][nc], candy[r][c] = candy[r][c], candy[nr][nc]

print(result)