### 1차 제출 오답 
N, M, B = map(int, input().split()) # N 세로 길이, M 가로 길이, B 인벤토리 블럭 개수
map_list = [list(map(int, input().split())) for _ in range(N)]
# print(map_list)
h_list = []
time = 0

# 최빈값 구하기
f_list = [0] * 257 # 높이가 0부터 256까지니까 256도 세주기 위해서
for i in range(N):
    for j in range(M):
        f_list[map_list[i][j]] += 1
        h_list.append(map_list[i][j]) # 최고값 찾으려고 미리 담아두기
        
mode = f_list.index(max(f_list)) # 최빈값

def flatten(mode, B):
    global h_list, time
    if mode < 0:
        return
    mode_value = mode
    # 최빈값보다 큰 수와의 차
    for idx in range(mode,max(h_list)+1): # 최빈값부터 최대값까지만 순회시키기
        if f_list[idx] == 0: # 값이 없으면 continue
            continue 
        else:
            B += abs(mode - idx)*f_list[idx]
            time += abs(mode - idx)*f_list[idx]*2

    # 만약 최빈값이 가장 낮은 땅이었다면 함수를 끝내고, 그렇지 않다면 낮은 값을 인벤토리의 블럭으로 채워줄 수 있는지 확인
    if mode == min(h_list):
        return mode_value
    else:
        count = 0 # 채울 때 필요한 블럭 수 
        for idx_2 in range(min(h_list),mode):
            if f_list[idx_2] == 0:
                continue
            else:
                count += (mode - idx_2)*f_list[idx_2]
        if B >= count:
            time += count
            return mode_value
        else:
            return flatten(mode-1, B)

m_v = flatten(mode, B)

print(time, m_v)

### 2차 제출 -- 시간초과, pypy로 제출하면 정답
import sys

N, M, B = map(int, input().split()) # N 세로 길이, M 가로 길이, B 인벤토리 블럭 개수
map_list = []
for _ in range(N):
    map_list.append([int(x) for x in sys.stdin.readline().rstrip().split()])
# 최소 작업량을 저장할 변수 ans를 큰 값으로 초기화
ans = int(1e9)
# 목표 높이를 저장할 변수 glevel 초기화
glevel = 0

# 높이를 0부터 256까지 (높이의 최대 범위) 반복
for i in range(257):  # i는 목표로 하는 땅의 높이
    use_block = 0  # 필요한 블록 수 (현재 높이를 목표 높이로 높이기 위해)
    take_block = 0  # 얻는 블록 수 (현재 높이를 목표 높이로 낮추기 위해)

    # 땅의 각 위치를 반복
    for x in range(N):
        for y in range(M):
            # 현재 위치의 높이가 목표 높이보다 높은 경우
            if map_list[x][y] > i:
                # 높이를 낮추기 위해 얻는 블록 수를 계산
                take_block += map_list[x][y] - i
            else:
                # 높이를 높이기 위해 필요한 블록 수를 계산
                use_block += i - map_list[x][y]

    # 사용해야 하는 블록 수가 현재 사용할 수 있는 블록 수보다 많은 경우
    if use_block > take_block + B:
        continue  # 다음 높이로 넘어감

    # 작업량을 계산 (높이 줄이는 데는 2배의 작업량이 필요, 높이는 1배)
    count = take_block * 2 + use_block

    # 계산된 작업량이 현재 최소 작업량보다 작거나 같은 경우
    if count <= ans:
        ans = count  # 최소 작업량 갱신
        glevel = i  # 목표 높이 갱신

# 최종 결과 출력 (최소 작업량, 목표 높이)
print(ans, glevel)