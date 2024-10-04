N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]
# print(*triangle, sep='\n')
floor = N - 2
while floor >= 0:
    for i in range(floor + 1):
        triangle[floor][i] += max(triangle[floor + 1][i], triangle[floor + 1][i + 1])
    # print(*triangle, sep='\n')
    floor -= 1
print(triangle[0][0])