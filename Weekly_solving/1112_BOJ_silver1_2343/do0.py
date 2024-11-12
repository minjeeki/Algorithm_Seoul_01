# 2343. 기타 레슨 (이분 탐색)

import sys
input = sys.stdin.readline

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2    # 이분 탐색
        sum_v = 0       # 현재 블루레이의 누적값
        cnt = 1         # 사용 블루레이 개수
        for i in range(N):
            if sum_v + arr[i] > mid:    # 지정한 블루레이 크기를 넘으면
                cnt += 1        # 블루레이 1장 더 사용
                sum_v = 0       # 초기화
            sum_v += arr[i]     # 블루레이 크기 누적값 증가
        if sum_v == 0:          # sum_v가 0이면 빈 블루레이
            cnt -= 1
        if cnt > M:         # 블루레이를 많이 쓰면
            start = mid + 1 # 크기를 크게
        else:
            end = mid - 1   # 아닐경우 크기를 작게
    return start

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)    # 블루레이의 최솟값
end = sum(arr)      # 블루레이의 최댓값
print(binary_search(start, end))