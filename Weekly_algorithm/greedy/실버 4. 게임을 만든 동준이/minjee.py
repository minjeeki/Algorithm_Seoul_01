N = int(input())
scores = [int(input()) for _ in range(N)]
total_minus = 0
for idx in range(N - 2, -1, -1):
    if scores[idx + 1] <= scores[idx]:
        total_minus += (scores[idx] - (scores[idx + 1] - 1))
        scores[idx] = scores[idx + 1] - 1
print(total_minus)