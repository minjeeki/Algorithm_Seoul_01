# 🔍 이진 탐색 (Binary Search)란?

![Binary Search](../../../assets/binary_search.webp)

- **정렬된 배열**에서 특정 값을 효율적으로 찾기 위한 알고리즘
- 중간 값을 확인하고, 찾는 값이 중간 값보다 크거나 작은지에 따라 탐색 범위를 절반으로 줄여나가는 방식

### ⏳ 이진 탐색의 시간 복잡도

- 시간 복잡도 : $O(logn)$
  - 단, 배열이 **정렬된 상태**여야만 사용 가능함

### 💻 이진 탐색 Basic Code

```python
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
```