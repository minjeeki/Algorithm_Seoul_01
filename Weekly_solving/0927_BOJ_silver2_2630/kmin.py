import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result_0 = 0
result_1 = 0
def make_paper(x,y,n):
    color = arr[x][y]   # 맨 처음 색
    global result_0, result_1
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color:  # 범위 내에 하나라도 색이 일치하지 않으면 계속 돌거야
                make_paper(x,y,n//2)
                make_paper(x+n//2, y, n//2)
                make_paper(x,y+n//2, n//2)
                make_paper(x+n//2, y+n//2, n//2)
                return
    if color == 0:      # 여기 부분 구현하는데 어려움을 겪음
        result_0+=1     # 흰종이에 +1
    else:
        result_1+=1     # 파랭이에 +1
make_paper(0,0,N)
print(result_0)
print(result_1)
