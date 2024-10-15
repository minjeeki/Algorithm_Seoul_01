K = int(input()) # 1제곱미터당 참외수
arr = [list(map(int, input().split())) for _ in range(6)]
direction = [0] * 5 # 동서남북 : 1,2,3,4 인덱스에 얼마나 나왔는지 저장
for i in arr:
    direction[i[0]] += 1    # 동서남북 각각 몇번씩 나왔는지 카운트
total_dir = []  # 동서남북 중 한번씩만 나온 거 찾기 (큰 너비 계산위해서)
minus_dir = []  # 두개 씩 나온 거 찾기 (뺄 면적 계산위해서)
for i in range(1, 5):
    if direction[i] == 1:   # 방향이 한번 나왔을 때
        total_dir.append(i)
    else:
        minus_dir.append(i) # 두개 이상 나왔을 때
first_land = []
for i in arr:
    if i[0] in total_dir:   # 방향이 한번 나온 거일 때
        first_land.append(i[1]) # 길이 추가
total_land = first_land[0] * first_land[1]  # 큰 너비 계산
second_land = []    # 뺄 면적 
for i in range(1, 5):
    if arr[i][0] in minus_dir and arr[i-1][0] in minus_dir and arr[i+1][0] in minus_dir:
        second_land.append(arr[i][1])   # 동서남북 중 두 개씩 나온 것들 중에서, 앞 뒤도 두개씩 나왔는지 확인하기
if arr[0][0] in minus_dir and arr[-1][0] in minus_dir and arr[1][0] in minus_dir:
    second_land.append(arr[0][1])   # 0번 인덱스일 경우 1번과 마지막 인덱스의 방향이 두번씩 나온 방향인지 확인하기
if arr[5][0] in minus_dir and arr[4][0] in minus_dir and arr[0][0] in minus_dir:
    second_land.append(arr[5][1])   # 마지막 인덱스의 경우 4번과 0번 인덱스 확인하기

minus_land = second_land[0] * second_land[1]
fin_land = total_land - minus_land  # 최종너비
fin_val = K * fin_land  # 면적 * 참외 수
print(fin_val)