
# 입력: N (남은 날짜)
N = int(input()) 

# 입력: 시간표, 각 날짜마다 [소요 기간, 수익]을 포함하는 리스트
timeTable = [list(map(int, input().split())) for _ in range(N)] 

# 재귀함수
def solve(i): 
    # 종료 조건: 현재 인덱스가 남은 날짜보다 크거나 같으면
    if i >= N: 
        return 0 # 더 이상의 날짜가 없으므로 수익은 0

    # 현재 인덱스 i에서 얻을 수 있는 최대 수익을 저장할 변수
    ret = 0 
    
    # 현재 날짜에서 상담을 진행할 수 있는지 체크
    # timeTable[i][0]: 소요 기간, timeTable[i][1]: 수익
    if i + timeTable[i][0] <= N: 
        # 상담을 진행할 경우: 다음 날짜는 현재 날짜 + 소요 기간
        # 수익은 현재 수익 + 상담 수익
        ret = solve(i + timeTable[i][0]) + timeTable[i][1] 
    
    # 상담을 진행하지 않고 다음 날짜로 넘어갈 경우
    # 현재 수익과 상담을 진행하지 않고 넘어갔을 때의 수익 중 최대값을 선택
    ret = max(ret, solve(i + 1)) 
    
    # 최대 수익을 반환
    return ret

# 재귀함수를 호출하여 결과를 출력
print(solve(0))
