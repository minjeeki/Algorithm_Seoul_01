'''
- 요구 사항 : 임의의 수열이 주어졌을 때 스택을 이용해서 수열을 만들 수 있는지, 있다면 어떤 순서로 push pop을 해야하는지 계산하는 프로그램 작성
    
- 입력 (형식)
    - line 1. n (스택에 넣을 수)
    - line 2 ~ line 2+n. 수열을 이루는 1 이상 n 이하의 정수 (중복 없음)
- 출력 (형식)
    - 수열을 만들기 위해 필요한 연산 출력
        - + : push / - : pop / 불가능한 경우 NO 출력
- 주요 아이디어 및 알고리즘 : 스택 / stack의 top은 targets[t_idx] 보다 항상 작거나 같다
- 코드 메모리 / 시간 : 45108KB / 2488ms
'''
n = int(input())
# 만들고 싶은 수열 넣기
targets = [0] * n
for i in range(n):
    targets[i] = int(input())
# 1부터 n까지의 숫자가 담긴 배열 생성
num_lst = list(range(1, n+1))
t_idx = 0
stack = []
commands = []
can_make = True
for num_idx in range(n):
    # 현재 숫자가 target 숫자보다 작을 경우 stack push
    if num_lst[num_idx] <= targets[t_idx]:
        stack.append(num_lst[num_idx])
        commands.append('+')
        # print(stack, stack[-1])
    # stack[top]이 target값과 동일할 경우, stack pop
    while len(stack) != 0 and targets[t_idx] == stack[-1]:
        stack.pop()
        commands.append('-')
        t_idx += 1
    # stack[top]이 target보다 큰 경우 또는 stack에 뭔가 남은 경우
    if len(stack) != 0 and stack[-1] > targets[t_idx]:
        can_make = False
        break
# 해당 수열 만들 수 있으면 여태까지의 명령어 모두 출력
if can_make:
    print(*commands, sep='\n')
else:
    print('NO')

''' jisulala7 코드
import sys
n = int(sys.stdin.readline())
stack=[]
answer = []
now = 1
FT = True
for i in range(n):
    num = int(sys.stdin.readline())
    # 스택 쌓기
    while now <= num:
        stack.append(now)
        answer.append("+")
        now += 1
    # 스택 꺼내기
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    # 불가능한 경우
    else:
        FT = False

# 스택 수열 만들수 있는지 여부에 따라 출력
if FT:
    for ans in answer:
        print(ans)
else:
    print('NO')
'''