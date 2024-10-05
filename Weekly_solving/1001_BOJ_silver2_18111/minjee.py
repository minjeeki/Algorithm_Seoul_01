# 스터디 끝나고 푼 코드 (2차원 배열 안 씀) => pypy3 / 120100KB / 380ms
N, M, B = map(int, input().split())     # N : 세로, M : 가로, B : 블록 개수
place = []
sum_place = 0
for _ in range(N):
    cur_lst = list(map(int, input().split()))
    place += cur_lst
    sum_place += sum(cur_lst)
min_time = 256 * N * M
that_height = 0
for hi in range(min(place), max(place) + 1):
    # 인벤토리 포함 전체 블록 수가 hi로 평탄화 후 블록 수보다 작으면 고려 안함
    if (hi * N * M) > (B + sum_place):
        continue
    time = 0
    for i in range(N * M):
        # 블록이 목표 높이와 동일 : 다음 반복문 진행
        if place[i] == hi:
            continue
        # 블록 꺼내 인벤 넣기 : 2초 소요
        elif place[i] > hi:
            time += (place[i] - hi) * 2
        # 인벤에서 블록 꺼내 쌓기 : 1초 소요
        elif place[i] < hi:
            time += (hi - place[i])
    # 최소 시간 발견 : 시간 및 높이 갱신
    if time < min_time:
        min_time = time
        that_height = hi
    # 최소 시간과 동일 상황 발생 : 최대 높이 갱신
    elif time == min_time:
        that_height = max(that_height, hi)
print(min_time, that_height)


# 효성님 코드 보고 다시 푼 것 (set 이용) => python / 156ms / 31120KB
N, M, B = map(int, input().split())
hi_dict = {}
min_time = 256 * N * M
height = 0

min_hi = 256
max_hi = 0
sum_place = 0
for _ in range(N):
    for hi in list(map(int, input().split())):
        hi_dict.setdefault(hi, 0)
        hi_dict[hi] += 1
        if min_hi > hi:
            min_hi = hi
        if max_hi < hi:
            max_hi = hi
        sum_place += hi

for tar_h in range(min_hi, max_hi + 1):
    if (tar_h * N * M) > (B + sum_place):
        continue
    time = 0
    for cur_h in hi_dict.keys():
        if cur_h == tar_h:
            continue
        elif cur_h > tar_h:
            time += (cur_h - tar_h) * hi_dict[cur_h] * 2
        elif cur_h < tar_h:
            time += (tar_h - cur_h) * hi_dict[cur_h]
    if time < min_time:
        min_time = time
        height = tar_h
    if time == min_time:
        height = max(height, tar_h)
print(min_time, height)

# 효성님 코드 => python / 132ms / 31120KB
N, M, B = map(int, input().split())
heights = {}
min_time = float('inf')

for _ in range(N):
    for height in list(map(int, input().split())):
        if height not in heights: # 높이를 key로, 그 높이의 땅의 개수를 value로 하는 딕셔너리 생성
            heights[height] = 0

        heights[height] += 1

heights = list(sorted(heights.items(), reverse=True)) # (key, value)를 내림차순으로 정렬한 리스트 생성
max_height, min_height = heights[0][0], heights[-1][0]

for num in range(min_height, max_height+1): # 최대, 최소 높이 범위 안의 임의의 높이에 대해
    inven = B
    time = 0

    for height in heights: # 현재 있는 땅의 높이가
        if height[0] > num: # 임의의 높이보다 크면
            amount = (height[0] - num) * height[1] # 떼어낼 땅의 개수
            time += amount * 2 # 2배만큼 시간 증가
            inven += amount # 그만큼 가지고 있는 땅 증가

        else: # 반대의 경우
            amount = (num - height[0]) * height[1] # 붙일 땅의 개수
            
            if inven >= amount: # 가지고 있는 땅의 개수가 그것보다 많으면
                time += amount
                inven -= amount

            else: # 아니라면 반복문 종료
                break

    else: # 반복문이 정상적으로 끝났다면
        if time <= min_time: # 걸린 시간이 최소 시간이면 변수 갱신
            min_time = time
            current_height = num

print(min_time, current_height)