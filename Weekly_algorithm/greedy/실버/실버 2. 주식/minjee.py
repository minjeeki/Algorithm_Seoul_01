'''
접근 순서
0. selling_point = 0, buy_cnt = 0, total_buy = 0 임의 지정
1. 마지막 인덱스 값부터 인덱스 0까지 순차적으로 돌기
2. selling point보다 크거나 같은 값 발생 시 selling point 업데이트, buy_cnt = 0 초기화
    - 이전 cnt_buy가 0보다 클 경우 이익 계산
3. selling point보다 작은 값 발생 시 total_buy += cur_stock, cnt_buy += 1
4. 순차 돌기 이후 cnt_buy가 0보다 클 경우 이익 계산

이 문제가 그리디인 이유 : 뒤에서부터 순차적으로 보면서 가장 최선의 선택 구함
'''

T = int(input())
for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    total_plus = 0
    selling_point = stocks[-1]
    cnt_buy = 0
    total_buy = 0
    for idx in range(N - 1, -1, -1):
        if stocks[idx] >= selling_point:
            if cnt_buy > 0:
                total_plus += (selling_point * cnt_buy - total_buy)
            total_buy = 0
            cnt_buy = 0
            selling_point = stocks[idx]
        else:
            cnt_buy += 1
            total_buy += stocks[idx]
    if cnt_buy > 0:
        total_plus += (selling_point * cnt_buy - total_buy)
    print(total_plus)
    
                
