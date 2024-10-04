import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
block = [list(map(int, input().split())) for _ in range(n)]

min_time = float('inf')  # 최소 시간을 무한대로 초기화
max_height = 0           # 가장 높은 높이를 0으로 초기화

start = min(map(min, block))
end = max(map(max, block))

for height in range(start, end+1):   # 블록의 최저~최고 높이에 대해 반복
    remove = add = 0        # 제거하고 추가해야 할 블록 수 초기화

    for i in range(n):      # 모든 땅의 면적 탐색
        for j in range(m):
            if block[i][j] > height:               # 현재 땅이 목표 높이보다 높으면 블록을 제거해야 함
                remove += block[i][j] - height
            else:
                add += height - block[i][j]        # 현재 땅이 목표 높이보다 낮으면 블록을 추가해야 함

    # 인벤토리 블록으로 작업이 가능한지 확인하기
    # (제거한 블록 + 초기 인벤토리 블록) >= 추가해야 할 블록
    if remove + b >= add:
        time = remove * 2 + add     # 시간 계산: 제거는 2초, 추가는 1초 소요

        if time <= min_time:        # 현재 계산된 시간이 최소 시간보다 작거나 같으면 업데이트
            min_time = time         # 시간이 같을 경우 더 높은 높이를 선택해야 하므로 기존의 최소 시간과 같더라도 업데이트
            max_height = height

print(min_time, max_height)
