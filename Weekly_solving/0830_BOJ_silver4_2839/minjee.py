N = int(input())

if N % 5 == 0:
    print(N // 5)
else:
    bongji = 0
    while N > 0:
        N -= 3
        bongji += 1
        if N % 5 == 0:
            bongji += N // 5
            print(bongji)
            break
        elif N == 1 or N == 2:
            print(-1)
            break
        elif N == 0:
            print(bongji)
            break