k = int(input())
r_list = []
c_list = []
num_list = []

for _ in range(6):                      # 육각형 -> 6번만 정보 받으면 됨
    d, num = map(int, input().split())  # 가로, 세로 각각 제일 긴 변을 구하기 위해 변의 방향에 따라 가로, 세로 리스트에 각각 저장
    if d == 3 or d == 4:                # 세로 변의 경우
        r_list.append(num)
    elif d == 1 or d == 2:              # 가로 변의 경우
        c_list.append(num)
    num_list.append(num)                # 빼야할 면적을 구하기 위해 모든 변의 길이를 리스트에 함께 저장

max_num1 = max(r_list)                  # 세로 변 중 제일 긴 변
max_num2 = max(c_list)                  # 가로 변 중 제일 긴 변

visited = [0]*6                         # 빼야할 면적 구하기 위한 리스트

# 제일 긴 변의 양 옆 변은 빼야할 면적의 변이 아님
# 위에서 구한 가로, 세로의 제일 긴 변과 해당 변의 좌 우 변은 visited에 체크하기
# 제일 긴 변과 해당 변의 양 옆을 체크하고 남은 (visited가 0인) 변의 곱이 빼야할 면적

# for i in range(6):
#     if i == 0:
#         if num_list[i] == max_num1 or num_list[i] == max_num2:
#             visited[0] = 1
#             visited[1] = 1
#             visited[5] = 1
#     elif i == 5:
#         if num_list[i] == max_num1 or num_list[i] == max_num2:
#             visited[4] = 1
#             visited[5] = 1
#             visited[0] = 1
#     elif num_list[i] == max_num1 or num_list[i] == max_num2:
#         visited[i] = 1
#         visited[i-1] = 1
#         visited[i+1] = 1

for i in range(6):
    if num_list[i] == max_num1 or num_list[i] == max_num2:
        visited[i] = 1
        visited[(i-1)%6] = 1
        visited[(i+1)%6] = 1

# 빼야 할 면적 구하기
# visted를 for문으로 순회하며 0인 인덱스 -> num_list의 인덱스로 사용하여 곱하기
empty = 1
for j in range(6):
    if visited[j] == 0:
        empty = empty * num_list[j]

size = max_num1 * max_num2

result = (size - empty) * k

print(result)