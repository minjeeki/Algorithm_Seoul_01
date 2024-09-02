n = int(input())

n_list = []     # 1 ~ n 까지의 수 리스트
for i in range(1, n+1):
    n_list.append(i)

inp_list = []   # 입력 받은 수 리스트
for _ in range(n):
    a = int(input())
    inp_list.append(a)

stack = []          # 스택 생성
result_list = []    # 연산자 담을 리스트
idx = 0             # 입력 받은 리스트의 인덱스 값

for i in n_list:
    stack.append(i)             # 스택에 수를 하나씩 넣기
    result_list.append('+')     # 넣을 때마다 연산자 리스트에도 해당하는 연산자 추가

    while stack[-1] == inp_list[idx]:   # 스택의 [-1] 값과 입력받은 리스트의 [0] 을 비교
        stack.pop()                     # 같은 건 스택에서 빼주기
        result_list.append('-')         # 연산자 리스트에도 해당하는 연산자 추가
        idx += 1                        # 0번 값 비교했으니 입력받은 리스트의 인덱스도 +1
        if len(stack) == 0:             # 만약 스택이 비었다면 멈추기
            break

if len(stack) != 0:     # 스택에 수가 남은 경우 -> 입력된 수열 만들기 불가
    print('NO')
else:
    result_list = '\n'.join(result_list)
    print(result_list)

# 처음에 idx 변수를 지정해주지 않고 입력받은 리스트에서 직접 pop했는데 인덱스 사용이 훨씬 편하다
# 스택의 제일 위 요소와 입력받은 리스트를 비교하는 과정에서 스택이 비었을 경우에 대한 조건을 쓰지 않았더니 무한루프가 돌았다