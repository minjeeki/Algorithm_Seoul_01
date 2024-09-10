def find(day, weight):
    global cnt
    if day == n:            # 운동키트 수 만큼의 날이 지났을 때,
        if weight >= 500:   # 중량이 500 이상이면
            cnt += 1        # cnt +1 하고 멈추기
        return

    if weight < 500:        # 운동 키트를 하루씩 쓰면서 하루라도 중량이 500 미만이 되면
        return              # 멈추기

    for i in range(n):          # n일 간 모두 다른 키트를 사용해야 함
        if visited[i] == 0:     # 만약 i번 키트를 쓴 적이 없다면
            visited[i] = 1      # i번 키트 사용하기
            find(day+1, weight - k + kit_list[i][1])    # 다음날로 넘어가기 -> weight 업데이트
            visited[i] = 0      # 사용 기록 지우기

n, k = map(int, input().split())        # n -> 운동 키트의 수, k -> 하루마다 감소하는 중량
arr = list(map(int, input().split()))

kit_list = []           # 각 운동키트 번호 별 중량 증가량을 담는 리스트
visited = [0]*(n+1)     # 운동키트 사용 기록

for i in range(n):
    kit_list.append([i+1, arr[i]])

cnt = 0     # 운동기간동안 항상 중량이 500 이상인 경우 카운트 할 변수
find(0, 500)

print(cnt)

# global 선언하지 않고 매개변수로 cnt를 받고 싶었는데 잘 안된다.. 연습해야지!