### 1차 아이디어 (시간초과) -- 하나씩 줄여가며 세어주기
'''
N, M = map(int, input().split()) # N 나무의 수, M 필요한 나무의 길이

tree_list = list(map(int, input().split()))

tree_list.sort(reverse=True)
# print(tree_list)

count = 0
H = tree_list[0]-1 # 절단기의 시작 높이는 나무의 가장 높은 길이 -1로 설정
while M > count: # 현재 자른 나무가 필요한 나무 길이와 같거나 보다 커지면 정지
    count = 0
    H -= 1
    for i in range(len(tree_list)):
        diff = tree_list[i] - H
        if diff > 0:
            count += diff
        else:
            break
print(H)
'''

### 2차 아이디어 (정답) -- 이진탐색

N, M = map(int, input().split())  # N: 나무의 수, M: 필요한 나무의 길이
tree_list = list(map(int, input().split()))

# 이진 탐색을 위한 변수 설정
low, high = 0, max(tree_list)
result = 0

while low <= high:
    mid = (low + high) // 2
    count = sum(tree - mid for tree in tree_list if tree > mid)

    if count >= M:  # 필요한 나무 길이보다 많거나 같으면
        result = mid  # 현재 높이를 결과로 저장
        low = mid + 1  # 더 높은 절단기 높이를 찾기 위해
    else:
        high = mid - 1  # 낮은 절단기 높이를 찾기 위해

print(result)
