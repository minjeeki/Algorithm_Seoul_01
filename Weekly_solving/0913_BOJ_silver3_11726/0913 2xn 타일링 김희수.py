import sys
sys.setrecursionlimit(10**9)

n = int(input())
memo = [0]*(n+1)

# n = (n-1) + (n-2) 라는 식이 나온다
# 처음에 memo 리스트 사용하지 않고 바로 재귀로 호출했더니 시간 너무 오래 걸림
# memo에 값 저장하며 재귀 호출 -> 메모이제이션인가 !?
# if memo[num] == 0 and num >= 3: -> 여기서 num >= 3 이 조건을 설정하지 않으면 인덱스 에러

def make(num):
    memo[1] = 1                         # 1, 2의 경우 n = (n-1) + (n-2) 식을 사용할 수 없음
    memo[2] = 2                         # 값 지정하고 시작
    if memo[num] == 0 and num >= 3:     # 만약 memo에 기록되지 않은 수면 재귀 호출하며 기록하기
        memo[num] = make(num-1) + make(num-2)
    return memo[num]                    # memo에 저장된 값 리턴

result = make(n) % 10007
print(result)