def paper(si, ei, sj, ej):  # 사각형 배열을 체크할 열과 행의 i, j좌표
    global blue, white      # 색종이 체크할 변수 global 선언
    cnt = 0                 # 다 같은 색인지 확인하는 변수
    size = (ei-si)*(ej-sj)  # 현재 함수에 입력받은 사각형 크기

    for i in range(si, ei):
        for j in range(sj, ej):     # 입력받은 좌표를 탐색
            cnt += arr[i][j]        # cnt에 현재 탐색하고 있는 사각형 좌표의 수를 다 더해줌

    if cnt == size:     # 현재 탐색하고 있는 사각형 좌표의 합이 사이즈와 같으면
        blue += 1       # 전체가 다 1로 채워져 있다는 뜻이기 때문에 이 사각형은 파란색 색종이이다
        return          # blue +1 해주고 리턴

    elif cnt == 0:      # 현재 탐색하고 있는 사각형 좌표의 합이 0이면
        white += 1      # 사각형 좌표 전체가 다 0이라는 뜻으로 이 사각형은 하얀색 색종이이다
        return

    else:
        mid_i = (si + ei) // 2       # 색종이가 아닌 경우
        mid_j = (sj + ej) // 2       # 나눠서 재귀함수 호출하기 위해 필요한 좌표값을 구해준다
        paper(si, mid_i, sj, mid_j)  # 왼쪽 위 탐색
        paper(si, mid_i, mid_j, ej)  # 오른쪽 위 탐색
        paper(mid_i, ei, sj, mid_j)  # 왼쪽 아래 탐색
        paper(mid_i, ei, mid_j, ej)  # 오른쪽 아래 탐색

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
blue = 0
white = 0

paper(0, n, 0, n)

print(white)
print(blue)