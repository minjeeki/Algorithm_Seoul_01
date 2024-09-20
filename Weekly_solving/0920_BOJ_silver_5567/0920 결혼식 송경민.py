N = int(input())
M = int(input())
lst = list([] for _ in range(N+1))

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)    # a의 친구 b를 lst index a에 b를 추가한다
    lst[b].append(a)    # 서로 친구관계라 했으므로 lst index b에 a를 추가
lst2 = []   # 여기에 본인 친구들 추가 할 거다
for i in lst[1]:
    lst2.append(i)
if len(lst2) == 0:  # 친구 없으면 0출력
    print(0)
else:
    lst3 = set()    # 세트는 중복이 허용되지 않으므로 list대신 set 사용, 여기에 친구 + 친구의 친구를 넣을 예정
    for i in lst2:
        lst3.add(i) # 본인 친구들 추가
    for i in lst2:
        for j in lst[i]:    # 친구의 친구 추가
            lst3.add(j)
    answer = len(lst3)-1    # 본인도 추가되어 있으므로 본인 제외
    print(answer)


