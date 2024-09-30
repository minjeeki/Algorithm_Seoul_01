def cut(x, y, n):
    global W, B
    color = paper[x][y] # 첫 번째 색

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]: # 현재 영역의 색이 첫 번째 색과 다르면
                cut(x, y, n // 2)        # 1사분면
                cut(x, y + n // 2, n // 2)      # 2사분면
                cut(x + n // 2, y, n // 2)      # 3사분면
                cut(x + n // 2, y + n // 2, n // 2)    # 4사분면
                return
    # 모든 색이 같으면 색에 따라 카운트
    if color == 0:
        W += 1
    else:
        B += 1


N = int(input())
first_N = N
paper = [list(map(int, input().split())) for _ in range(N)]

# print(arr2)

B, W = 0, 0
cut(0,0,N)

print(W)
print(B)