# 3085. 사탕 게임 (구현, 완탐)

import sys
input = sys.stdin.readline  # 입력 시간을 단축하기 위한 함수

# 아래, 오른쪽으로 바꿔볼 함수
def change():
    global max_v  # 최대 연속 길이를 저장하는 전역 변수
    for i in range(N):
        for j in range(N):
            # 아래값이 범위 내이고 / 현재값과 값이 다를 경우
            if i + 1 < N and arr[i][j] != arr[i + 1][j]:
                arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j] # 아래와 교환
                check_max_v()                                       # 바꾸고 연속된 최댓값을 체크
                arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j] # 원래 상태로 되돌림

            # 오른쪽값이 범위 내이고 / 현재값과 값이 다를 경우
            if j + 1 < N and arr[i][j] != arr[i][j + 1]:
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
                check_max_v()
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
    return max_v  # 최대 연속 길이를 반환

max_v = 0   # 최댓값 변수 초기값 선언
# 가로, 세로 중 가장 긴 연속 부분의 최댓값을 찾는 함수
def check_max_v():
    global max_v

    for i in range(N):  # 가로체크
        tmp = 0
        prev = arr[i][0]    # 이전값을 저장할 prev 변수의 초기값 선언
        for j in range(N):
            if arr[i][j] == prev:
                tmp += 1    # 연속된 경우 길이 증가
                max_v = max(max_v, tmp)  # 최대값 갱신
            else:
                tmp = 1         # 다른 값이 나오면 연속 길이 초기화
            prev = arr[i][j]    # 이전 값을 현재 값으로 업데이트

    for j in range(N):  # 세로체크
        tmp = 0
        prev = arr[0][j]    # 이전값을 저장할 prev 변수의 초기값 선언
        for i in range(N):
            if arr[i][j] == prev:
                tmp += 1
                max_v = max(max_v, tmp)
            else:
                tmp = 1
            prev = arr[i][j]
    return max_v

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
print(change())