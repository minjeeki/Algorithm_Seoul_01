# 처음 시도한 방법
# 재귀 + 가지치기 했으나 시간초과 ..

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# num_list = []
#
# def triangle(level, num, plus_n):
#     if level == n:
#         num_list.append(plus_n)
#         return
#
#     if len(num_list) != 0:
#         if plus_n + ((n-level)*9999) < max(num_list):
#             return
#
#     triangle(level + 1, num, plus_n + arr[level][num])
#     triangle(level + 1, num + 1, plus_n + arr[level][num])
#
#
# triangle(0, 0, 0)
# print(max(num_list))

# 메모이제이션 사용

import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
memo = [[-1]*n for _ in range(n)]
max_num = 0

def triangle(level, num):       # level -> 삼각형의 몇 번째 행인지, num -> 현재 행의 위치
    global max_num              # 함수 내에서 수정되는 변수 global 선언

    if level == n:              # 삼각형의 전체 높이만큼 진행 후엔 더 이상 더할 값이 없음 -> 0 리턴
        return 0

    if memo[level][num] != -1:  # 이미 계산된 값이 있다면 그 위치에서 나올 수 있는 최대 수라는 뜻 -> 해당 값 반환
        return memo[level][num]

    now_sum = arr[level][num] + max(triangle(level+1, num), triangle(level+1, num+1))
    memo[level][num] = now_sum  # 현재 위치의 값 + 갈 수 있는 양쪽 경로 중 더 큰 값 더해서 memo에 저장

    return now_sum

triangle(0, 0)
print(triangle(0, 0))