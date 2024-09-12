N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A와 B 오름차순 정렬 후 서로 곱함
A.sort(reverse=True)
B.sort()
result = 0
for idx in range(N):
    result += (A[idx] * B[idx])
print(result)