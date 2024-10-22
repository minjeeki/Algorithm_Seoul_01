# 가로라인 내 최댓값 확인
def check_row(xi):
    # 초기 설정
    max_candy = 0
    check_row_cur = 1
    before_color = boards[xi][0]
    # 최대 연속 색 확인
    for i in range(1, N):
        if before_color == boards[xi][i]:
            check_row_cur += 1
        else:
            before_color = boards[xi][i]
            max_candy = max(max_candy, check_row_cur)
            check_row_cur = 1
        if max_candy == N:
            return max_candy
    return max(max_candy, check_row_cur)

# 세로라인 내 최댓값 확인 (로직은 가로와 동일하나 확인하는 라인 차이 존재)
def check_col(yi):
    # 초기 설정
    max_candy = 0
    check_col_cur = 1
    before_color = boards[0][yi]
    # 최대 연속 색 확인
    for i in range(1, N):
        if before_color == boards[i][yi]:
            check_col_cur += 1
        else:
            before_color = boards[i][yi]
            max_candy = max(max_candy, check_col_cur)
            check_col_cur = 1
        if max_candy == N:
            return max_candy
    return max(max_candy, check_col_cur)

# 인접 값 변경 후 변경 결과 확인
def change_near(boards):
    max_candy = 0
    for xi in range(N):
        for yi in range(N):
            for di in range(LEN_D):
                nx = xi + dx[di]
                ny = yi + dy[di]
                if 0 <= nx < N and 0 <= ny < N and boards[xi][yi] != boards[nx][ny]:
                    # 자리 교환
                    boards[xi][yi], boards[nx][ny] = boards[nx][ny], boards[xi][yi]
                    # 가로 확인
                    max_candy = max(max_candy, check_row(xi))
                    if max_candy == N:
                        return max_candy
                    # 세로 확인
                    max_candy = max(max_candy, check_col(yi))
                    if max_candy == N:
                        return max_candy
                    # 변경 사항 원위치
                    boards[xi][yi], boards[nx][ny] = boards[nx][ny], boards[xi][yi]
    return max_candy

N = int(input())
boards = [list(input()) for _ in range(N)]
# 상하좌우를 모두 살펴볼 필요는 없음 (상, 좌는 이미 앞전 단계에서 진행했기 때문)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
LEN_D = 4
max_candy = 0
# 변경 전 기준 max_candy 파악
for i in range(N):
    max_candy = max(max_candy, check_row(i))
    max_candy = max(max_candy, check_col(i))
    if max_candy == N:
        print(max_candy)
        break
# 자리 교환 진행
if max_candy < N:
    max_candy = max(max_candy, change_near(boards))
    print(max_candy)