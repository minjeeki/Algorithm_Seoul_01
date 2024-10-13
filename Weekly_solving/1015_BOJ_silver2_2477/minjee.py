K = int(input())
list_len = []
max_width = 0
max_height = 0
for i in range(6):
    list_len.append(list(map(int, input().split())))
    if list_len[i][0] in {1, 2}:
        max_width = max(max_width, list_len[i][1])
    elif list_len[i][0] in {3, 4}:
        max_height = max(max_height, list_len[i][1])
list_len += list_len
minus_width = 0
minus_height = 0
for idx in range(1, 11):
    if list_len[idx][1] == max_width and list_len[idx][0] in {1, 2}:
        minus_width = max(list_len[idx - 1][1], list_len[idx + 1][1]) - min(list_len[idx - 1][1], list_len[idx + 1][1])
    if list_len[idx][1] == max_height and list_len[idx][0] in {3, 4}:
        minus_height = max(list_len[idx - 1][1], list_len[idx + 1][1]) - min(list_len[idx - 1][1], list_len[idx + 1][1])
    if minus_width != 0 and minus_height != 0:
        break
print(((max_height * max_width) - (minus_height * minus_width)) * K)