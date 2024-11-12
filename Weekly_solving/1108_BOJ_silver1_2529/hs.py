def num_check(x, y, oper):  # 앞, 뒤 숫자와 부등호 비교하는 함수
    if oper == '<':         # 두 숫자와 부등호 비교
        if x > y:           # 조건을 만족하지 않으면 false 반환하여
            return False    # dfs 함수의 조건 통과되지 않도록!
    else:
        if x < y:
            return False
    return True


def dfs(n, level):              # 숫자 조합하는 함수
    if level == k + 1:          # 주어진 수를 다 채웠을 때
        result_list.append(n)   # 결과 리스트에 현재 수 추가
        return

    for i in range(10):         # 모든 수의 조합 만들기
        if visited[i] == 0:     # 방문하지 않고, 첫 번째 숫자거나 위 함수에서 true를 반환했다면 계속해서 수 조합
            if n == '' or num_check(n[level-1], str(i), oper[level-1]):
                visited[i] = 1
                dfs(n + str(i), level + 1)
                visited[i] = 0

k = int(input())
oper = list(input().split())

visited = [0] * 10
result_list = []
dfs('', 0)

result_list.sort()      # 만들어진 모든 수 중 제일 큰 수와 작은 수를 출력해야 함
print(result_list[-1])  # 리스트 정렬 후 인덱스 활용하여 프린트하기
print(result_list[0])