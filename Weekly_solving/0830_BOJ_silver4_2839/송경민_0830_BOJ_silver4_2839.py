N = int(input())
num = N//5    # 가장 작은 횟수가 나오려면 5로 최대한 많이 퍼야 된다
for i in range(num,-1, -1): # 위와 같은 이유로 num부터 0까지 역순으로 돈다
    if (N-i*5)%3 == 0:   # 5,3으로 나눠지면 횟수가 최소이므로 answer구하고 break
        t = (N-i*5)//3
        answer = i + t
        break
    else:
        answer = -1
print(answer)
