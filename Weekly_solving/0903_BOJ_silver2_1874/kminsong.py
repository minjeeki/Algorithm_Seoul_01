n = int(input())
arr=[]  # 오름차순으로 넣으면서 check_arr에 맞게 만들거야
check_arr = []  # 만들어야 되는 리스트
# for i in range(1, n+1):
#     arr.append(i)
for _ in range(n):
    num = int(input())
    check_arr.append(num)
start = 0   # check_arr의 인덱스 값
start2= 1   # arr에 추가되는 값 : 1부터 시작, 조건 만족하면 1씩 증가, 최대 n까지
fin_lst = []
result = True   # result가 True이면 fin_lst 출력, False이면 NO출력
while start <= n-1: # start가 마지막이 될때까지
    if len(arr)==0: # arr이 비어있으면 추가
        arr.append(start2)
        fin_lst.append('+')
        start2+=1   # 오름차순 입력 그다음거로 가자
    elif arr[-1] < check_arr[start] and arr[-1] != check_arr[start]:   # 마지막이 check_arr값보다 작으면서 같지 않으면
        arr.append(start2)
        fin_lst.append('+')
        start2+=1
    elif arr[-1] > check_arr[start] and arr[-1]!= check_arr[start]: # arr마지막 값이 check보다 큰 경우 절대 만들 ㅅ후 없다
        result = False
        break
    else:   # arr[-1]이 check_arr[start]와 같은 경우
        arr.pop()
        fin_lst.append('-')
        start+=1
    # start2+=1
    # start2+=1
if result == True:
    for i in fin_lst:   # fin_lst를 돌면서 print
        print(i)
else:
    print('NO')


