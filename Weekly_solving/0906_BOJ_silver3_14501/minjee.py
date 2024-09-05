'''
* 주요 아이디어 : 
* 생각한 알고리즘 : 백트래킹, 재귀 / 싫다면 노가다 (브루트포스, 완전 탐색)

'''

N = int(input())            # N : 상담 받을 수 있는 일자 개수
work_lst = [[]] * (N + 1)   # work_lst : 일자, 기간, 보수의 2차원 리스트
# 입력값 받기
for idx in range(1, N + 1):
    counsel_dates, counsel_pay = map(int, input().split())
    word_lst[idx] = [idx, counsel_dates, counsel_pay]
max_pay = 0
# 일자별 다음 일자에 할 수 있는 모든 선택 따지기
for choice_1st in range(1, N + 1):