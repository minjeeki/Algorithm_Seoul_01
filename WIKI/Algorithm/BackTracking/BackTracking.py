# 백트래킹 Basic Code

N, M = map(int, input().split())

path = []
def back_tracking():
    # 기저조건 : 함수가 끝나는 조건을 설정
    if len(path) == M:       # 배열의 길이를 확인
        print('기저 조건을 만족 시 여기서 추가 작업')
        return 
    
    # 기저조건을 통과하지 못하면 탐색 시작
    for i in range(1, N+1):
        # 유망한 노드인지 확인 (DFS와의 차이점)
        if i not in path:   # 중복 확인 (필요하다면)
            path.append(i)      # 배열 추가
            back_tracking()     # 재귀
            path.pop()          # 재귀 탐색을 한후 pop을 하면서 되돌아감 (백트래킹)
back_tracking()

# 위 코드에서 for문으로 탐색하는 범위는 1~N으로 range()함수를 통해 탐색하지만,
# 문제에 따라 필요 시 배열(list)안에 탐색해야 할 원소들을 저장하고
# 그 배열을 순회함으로써 탐색이 가능함.