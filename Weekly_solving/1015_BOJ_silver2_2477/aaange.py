# 참외 밭


cham = int(input()) # 한 제곱당 참외 개수

arr = [list(map(int, input().split())) for _ in range(6)]

# print(arr)

# 가장 큰 값 찾기
# max_value = max(arr[1])
max_value = 0
max_idx = 0
for i in range(6):
    if arr[i][1] > max_value:
        max_value = arr[i][1]
        max_idx = i

# 다른 변의 길이
# max_2_value = max(arr[max_idx-1][1], arr[max_idx+1][1])
if max_idx != 5:
    max_2_value = max(arr[max_idx-1][1], arr[max_idx+1][1])
else:
    max_2_value = max(arr[4][1], arr[0][1])


if max_idx != 5:
    max_2_idx = max_idx - 1 if max_2_value == arr[max_idx - 1][1] else max_idx + 1
else:
    max_2_idx = 4 if max_2_value == arr[max_idx -1][1] else 0

# print(max_2_value)
# print(max_2_idx)

## 전체 사각형의 넓이
total_area = max_value * max_2_value

# print(total_area)

# 
if max_2_idx == max_idx -1 :
    if max_2_idx != 0:
        value_1 = arr[max_2_idx-1][1]
        if max_2_idx -1 != 0:
            small_2_value = arr[max_2_idx-2][1]
        else:
            small_2_value = arr[5][1]
    else: 
        value_1 = arr[5][1]
        small_2_value = arr[4][1]
else:
    if max_2_idx != 5:
        value_1 = arr[max_2_idx+1][1]
        if max_2_idx + 1 != 5:
            small_2_value = arr[max_2_idx+2][1]
        else:
            small_2_value = arr[0][1]
    else:
        value_1 = arr[0][1]
        small_2_value = arr[1][1]

small_value = max_value - value_1

small_area = small_value * small_2_value

area = total_area - small_area

print(area*cham)

