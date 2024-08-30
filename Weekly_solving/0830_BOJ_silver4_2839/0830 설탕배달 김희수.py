n = int(input())

count = 0       # 봉지 개수를 저장할 변수
found = True    # '-1'를 출력할 경우에 대한 플래그

if n % 5 != 0:  # 만약 n이 5로 나눠지지 않을 때
    a = n // 5
    b = n % 5
    count += a  # 5로 나눈 몫을 count에 저장

    if b % 3 != 0:              # 5로 나눈 나머지 수(b)를 3으로 나눴을 때, 나머지가 있는 경우
        while b % 3 != 0:       # b가 3으로 나누어 떨어질 때까지 봉지 개수 -1, b +5 반복하기
            if count == 0:      # 만약 봉지 개수가 0이 됐다면 3으로 나누어 떨어지는 수가 아니기 때문에
                found = False   # 플래그를 False로 설정
                break
            count -= 1
            b += 5

        if b % 3 == 0:          # 만약 3으로 나누어 떨어지는 경우
            count += b // 3     # count에 해당 몫 추가

    else:                       # 처음부터 3으로 나누어 떨어지는 경우
        count += b // 3
else:                           # 처음 입력받은 n이 5로 나누어 떨어지는 경우
    count += n // 5

if found == False:
    print('-1')
else:
    print(count)