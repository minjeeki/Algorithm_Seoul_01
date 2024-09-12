S = list(input())

len_s = len(S)
min_cnt = len_s
# 전체를 1로 만들기
idx = 0
cnt_1 = 0
while idx < len_s:
    if S[idx] == '0':
        while idx < len_s and S[idx] == '0':
            idx += 1
        cnt_1 += 1
    idx += 1
# 전체를 0으로 만들기
idx = 0
cnt_0 = 0
while idx < len_s:
    if S[idx] == '1':
        while idx < len_s and S[idx] == '1':
            idx += 1
        cnt_0 += 1
    idx += 1
print(min(cnt_1, cnt_0))