N = int(input())

# 입력값 받기 & 정렬
time_table = [list(map(int, input().split())) for _ in range(N)]
# print(time_table)
time_table.sort(key=lambda x: (-x[1], -x[0]))
# print(time_table)

# 뒤에서부터 접근하며, 그리디 & total_cnt 세기
total_cnt = 1
cur_time = time_table[0]
for time1 in time_table[1:]:
    # cur_time의 s_time보다 time1의 e_time이 큼 (cur_time과 겹쳐진 상황)
    if cur_time[0] < time1[1] and cur_time[0] < time1[0]:
        cur_time = time1
        # print(time1, 'cur_time switch')
    # time1의 e_time이 cur_time의 s_time보다 작거나 같을 경우
    elif time1[1] <= cur_time[0] and time1[1] <= cur_time[1]:
        cur_time = time1
        total_cnt += 1
        # print(time1, 'total_cnt +!')
    # else:
        # print(time1, cur_time, 'nothing')
print(total_cnt)

'''예외
3
1 100
100 200
99 101      정답 : 2

3
4 4
3 4
2 4         정답 : 2

2
1 1
2 2         정답 : 2

5
1 3
1 4
4 4
4 4
4 5         정답 : 4

1
0 0         정답 : 1
'''

'''타인 코드인데 알고보니 경민이었던 건에 대하여
import sys
input = sys.stdin.readline
N = int(input()) # 회의 N개
time = []
for _ in range(N):
    st, et = map(int,input().split())   # 시작, 끝 시간
    time.append((st, et))
time.sort(key= lambda x : (-x[1],-x[0]))
start_time, end_time = time.pop()
cnt = 1
while len(time) >=1:
    start_t, end_t = time.pop()
    if end_time <=start_t:
        cnt+=1
        start_time, end_time = start_t, end_t
print(cnt)
'''

''' tsuyu (272ms / 53576KB)
from sys import stdin
def input():
    return stdin.readline().rstrip()

from collections import deque

n = int(input())
meetings = []
for _ in range(n):
    a, b = map(int, input().split())
    meetings.append((a, b))
meetings.sort(key=lambda x:(x[1], x[0]))

end = 0
ans = 0

for a, b in meetings:
    if a >= end:
        ans += 1
        end = b
print(ans)
'''