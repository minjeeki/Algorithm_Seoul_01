def find(point, money):             # point -> 전체 기간 중 현재 일수, money -> 상담 금액
    if point >= n:                  # 현재 일수가 전체 기간(마지막 날)과 같거나 크다면 더 이상 상담하지 못함
        money_list.append(money)    # 최대 수익을 구하기 위한 리스트에 넣고 return
        return

    find(point + 1, money)  # 현재 날짜에 잡힌 상담을 하지 않고 넘어가기 (+1 로 모든 경우의 수를 재귀함수로 구현)

    if point + arr[point][0] <= n:  # 현재 날짜에 잡힌 상담 기간동안은 다른 상담 불가 -> 현재 날짜 + 상담기간이 전체 일수보다 크면 안됨
        find(point + arr[point][0], money + arr[point][1])  # 조건을 만족하면 재귀함수로 다음 상담을 할 수 있는 날로 인자 넣어주기

# ============== 실패한 재귀 함수 ==============
# def find(point, money):
#     if point >= n:
#         money_list.append(money)
#         return
#
#     for i in range(point, n):         # 모든 경우의 수를 구하려고 for문을 썼는데, 간단하게 현재 날짜에 +1 하면 되는 거였다
#         if point + arr[i][0] > n:     # 현재 위치부터 종료일까지 갈 수 있는 모든 날짜 방문
#             money_list.append(money)
#             break                     # 여기서 break로 for문이 끝나니까 다음 i의 경우를 고려할 수 없어서 그런가?ㅜㅜ
#         money = money + arr[i][1]     # 업데이트
#         point = point + arr[i][0]     # 업데이트
#         find(point, money)            # 업데이트 한 수로 재귀함수 호출
# ===========================================

n = int(input())
arr = []
money_list = []
for i in range(n):
    day, cash = map(int, input().split())
    arr.append([day, cash])

find(0, 0)
print(max(money_list))
