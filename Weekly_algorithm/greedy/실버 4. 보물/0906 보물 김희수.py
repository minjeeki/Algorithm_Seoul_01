n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 최솟값을 구해야 함
# a는 오름차순, b는 내림차순으로 정렬하여, 각 같은 인덱스 위치의 숫자를 곱해줌
a = sorted(a)
b = sorted(b)[::-1]
num = 0
for i in range(n):
    num += a[i] * b[i]

print(num)