expression_lst = input().split('-')
len_lst = len(expression_lst)
for idx in range(len_lst):
    cur_sum = 0
    cur_lst = expression_lst[idx].split('+')
    for num in cur_lst:
        cur_sum += int(num)
    expression_lst[idx] = cur_sum
result = expression_lst[0]
for idx in range(1, len_lst):
    result -= expression_lst[idx]
print(result)