import sys
import itertools, copy
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
n = N//2
lst = []    # 저번에 민지누나가 연속된 숫자들어간 리스트 만드는법 알려줬는데 까먹음 ^^7
for i in range(N):
    lst.append(i)

lst2 = list(itertools.combinations(lst, n)) # 조합으로 쫙 만들어
min_val = float('inf')
for i in lst2:  # 굳이 다 안돌고 절반만 돌아도 될거 같음
    lst3 = copy.deepcopy(lst)   # 그냥 같다고 했다가 계속 틀림, 깊은 복사해야 한다
    val = 0
    val2 = 0
    for j in i: # 조합에 있는 것들의 합
        lst3.remove(j)
        for t in i:
            if j != t:  # (j,j)이런 형식을 제외시켜야 하므로
                val += arr[j][t]

    for x in lst3:  # 조합에 안들어 있는 것들의 합
        for y in lst3:
            if x != y:
                val2 += arr[x][y]
    if abs(val - val2) <= min_val:  # val이 클수도 작을수도 있으므로 abs
                min_val = abs(val - val2)
print(min_val)
    
