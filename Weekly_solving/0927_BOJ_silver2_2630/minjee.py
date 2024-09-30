def ft_check_square(sx, sy, size):
    global total_cnt_white, total_cnt_blue

    cnt_white = 0
    cnt_blue = 0
    # 현재 확인하는 범위 내는 모든 값이 0 또는 1 이어야 진행 의미가 있음
    for i in range(sx, sx + size):
        for j in range(sy, sy + size):
            if grid[i][j] == 0:
                cnt_white += 1
            else:
                cnt_blue += 1
        # cnt_white와 cnt_blue가 둘 다 0이 아니면 분할 필요
        if cnt_white != 0 and cnt_blue != 0:
            # 현재 범위 내에서 쪼개서 시작점 잡기
            for nx in range(sx, sx + size, size // 2):
                for ny in range(sy, sy + size, size // 2):
                    ft_check_square(nx, ny, size // 2)
            return
    if cnt_white == size * size:
        total_cnt_white += 1
    elif cnt_blue == size * size:
        total_cnt_blue += 1


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 전체 개수 확인
total_cnt_white = 0
total_cnt_blue = 0

ft_check_square(0, 0, N)
print(total_cnt_white, total_cnt_blue, sep='\n')