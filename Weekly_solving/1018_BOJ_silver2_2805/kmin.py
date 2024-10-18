N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)  # 이분탐색을 위한 시작과 끝
result = 0

while start <= end: # 이분탐색
    mid = (start + end) // 2
    total = 0
    for i in trees:
        if i > mid:
            total += i - mid    # 잘린 나무 길이 전부 추가
    
    if total >= M:  
        result = mid  
        start = mid + 1
    else:
        end = mid - 1

print(result)