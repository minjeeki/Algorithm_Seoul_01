def find_max(power):
    global result

    if len(arr) == 2:                   # 구슬을 다 제거하고 양 끝 두개가 남았을 때
        result = max(result, power)     # 기존의 result 값과 현재 값인 power 비교 후 갱신
        return

    for i in range(1, len(arr)-1):      # 양 끝 구슬은 제외하고 탐색
        plus = arr[i-1] * arr[i+1]      # 에너지 구하기 -> 현재 위치 양 옆 구슬 에너지 곱하기
        c = arr.pop(i)                  # 현재 위치 구슬 제거하기 -> 변수에 할당한 이유는 재귀 함수 호출 후 원복 필요하기 때문
        find_max(power + plus)          # power 업데이트하고 재귀 함수 호출
        arr.insert(i, c)                # 제거했던 구슬 다시 리스트에 넣기

n = int(input())
arr = list(map(int, input().split()))
result = 0      # 최대 에너지 값을 저장할 변수
find_max(0)
print(result)