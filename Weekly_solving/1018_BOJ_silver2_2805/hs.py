def cut(arr, start, end):

    if start > end:     # 기저조건 : start가 end를 넘어서면 탐색 종료
        return end      # 제일 큰 값 반환 -> end 반환

    mid = (start + end) // 2    # 중간 지점 탐색

    sum_tree = 0                    # 위에서 찾은 중간 지점(mid)을 기준으로 나무를 잘랐을 때 얻을 수 있는 나무 총 길이 계산
    for i in arr:                   # 모든 나무를 순회하며
        if i > mid:                 # 중간 지점보다 큰 나무의 경우
            sum_tree += i - mid     # 잘라서 sum_tree에 더하기

    if sum_tree == m:               # 잘라낸 나무의 총 길이가 m인 경우
        return mid                  # 현재 절단 높이(mid) 반환

    elif sum_tree > m:                  # 잘라낸 나무의 총 길이가 m보다 큰 경우
        return cut(arr, mid+1, end)     # 더 높은 절단 높이에서 탐색

    elif sum_tree < m:                  # 잘라낸 나무의 총 길이가 m보다 작은 경우
        return cut(arr, start, mid-1)   # 더 낮은 절단 높이에서 탐색

n, m = map(int, input().split())
tree = list(map(int, input().split()))
result = cut(tree, 0, max(tree))
print(result)