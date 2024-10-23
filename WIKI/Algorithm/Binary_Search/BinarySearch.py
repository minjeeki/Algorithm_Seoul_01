def binary_search(target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:  # 중간값이 타겟과 일치할 때
            return mid
        elif arr[mid] > target: # 중간값이 타겟보다 클 때
            right = mid - 1
        else:   # 중간값이 타겟보다 작을 때
            left = mid + 1
    return      # 값을 찾을 수 없는 경우 False

# 예시 사용
arr = [1, 3, 5, 7, 9, 11, 13, 15]
arr.sort()    # 이진 탐색은 항상 배열이 정렬되어있어야 함
target = 7
result = binary_search(target)
print(result)   # 인덱스 번호를 출력, 찾지 못했다면 False를 출력