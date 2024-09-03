def stack_sequence():
    N = int(input().strip())
    sequence = [int(input().strip()) for _ in range(N)]
    # print(sequence)

    stack = []
    result = []
    current = 1

    # 목표 수열의 각 숫자에 대해 반복
    for num in sequence:
        # 목표 숫자(num)까지의 숫자를 스택에 푸시
        while current <= num:
            stack.append(current)
            result.append('+')
            current += 1
        
        # 스택의 상단 숫자가 목표 숫자(num)와 일치하는 경우, 팝
        if stack and stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            # 스택의 상단 숫자가 목표 숫자(num)와 일치하지 않는 경우, 수열을 만들 수 없으므로 "NO"를 출력하고 종료
            print("NO")
            return

    # 모든 수열을 처리한 후, 줄 바꿈으로 구분하여 출력
    print("\n".join(result))

stack_sequence()