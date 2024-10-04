import sys
input = sys.stdin.readline


N, M, B = map(int, input().split()) # B가 인벤토리에 있는 스페어 블록
arr = [list(map(int, input().split())) for _ in range(N)]
numbers = [0] * 257
### 1차 틀림, 주어진 테케는 맞음 but 제출은 틀림
# result_1 = 0
# result_2 = 0
# for i in range(N):
#     for j in range(M):
#         numbers[arr[i][j]] += 1
# max_num_height = max(numbers)  # 최빈값을 갖고 있는 number의 갯수
# max_index = numbers.index(max_num_height)   # 최빈값
# x = 0   # 쌓는다
# y = 0   # 뺀다
# min_num = 256 # 스페어 블록이 부족할 경우 전부 빼야 하므로 그 때의 높이는 현재의 미니멈 높이가 된다
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] <= min_num:
#             min_num = arr[i][j]
#         if max_index>arr[i][j]:
#             x += abs(max_index-arr[i][j])
#         else:
#             y += abs(max_index-arr[i][j])

# if x <= B:  # 쌓는데 쓴 블록 갯수가 주어진 스페어보다 작거나 같을때
#     result_1 = x + 2*y
#     result_2 = max_index
#     print(result_1, result_2)
# else:
#     result_1 = 0
#     result_2 = min_num
#     for i in range(N):
#         for j in range(M):
#             result_1 += abs(min_num - arr[i][j])
#     print(result_1, result_2)

### 2차 python은 시간초과, pypy는 pass
result = []
for height in range(257):   # 높이를 0부터 256까지 다 돌릴 거다
    x = 0   #쌓는다
    y = 0   #뺀다
    for i in range(N):
        for j in range(M):
            if arr[i][j] < height:  # 블록을 쌓아야 되는 경우
                x += abs(arr[i][j] - height)    # 그냥 abs로 계산
            else:                   # 블록을 빼거나 아무 조작 안하는 경우
                y += abs(arr[i][j] - height)

    if x <= B + y:  # 여기서 여러번 틀림, 스페어 블록에 뺀 블록이 추가 되는 걸 생각치 못함
        a = x + 2*y     # 걸리는 시간
        result.append((a,height))   # set()로 추가, (시간, 높이)
min_val = 0
for i in range(len(result)):
    if result[i][0] <= result[min_val][0]: # 작다가 아닌 작거나 같아야 되는 이유는 답이 여러개 일때 최고 높이 출력
        min_val = i
print(result[min_val][0], result[min_val][1])