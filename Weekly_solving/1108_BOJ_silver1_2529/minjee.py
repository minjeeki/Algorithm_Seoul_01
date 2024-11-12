# 재귀 코드
def move_next(range_start, range_end, cur_idx):
    for next_num in range(range_start, range_end):
        if not visited[next_num]:
            visited[next_num] = True
            num_lst.append(next_num)
            dfs(next_num, cur_idx + 1)
            visited[next_num] = False
            num_lst.pop()

def dfs(cur_num, cur_idx):
    # 초기 작업
    if cur_num == -1:
        move_next(0, 10, cur_idx)
        return
    # 기저 조건 (가지치기는 알아서 당하고 있음)
    if cur_idx == k:
        answers.append(''.join(list(map(str, num_lst))))
        return
    
    # 부등호값에 따라 for문 범위 달리해서 재귀 작업
    if signs[cur_idx] == '<':
        move_next(cur_num + 1, 10, cur_idx)
    elif signs[cur_idx] == '>':
        move_next(0, cur_num, cur_idx)

# 문제 입력값 처리
k = int(input())
signs = input().split()

# 방문 처리, 정답되는 모든 것 나열 (0부터 순차 시작하니 자동 오름차순 정렬), 값 임시 저장소
visited = [False] * 10
answers = []
num_lst = []

dfs(-1, -1)
print(answers[-1], answers[0], sep='\n')

'''블로그 코드
- 인상적이었던 점 : dfs의 매개변수 처리에서 num_lst를 통한 제어가 아닌 str을 이용할 수 있다는 것

def check(a, b, op):
  if op == '<':
    if a > b: return False
  if op == '>':
    if a < b: return False
  return True

def dfs(cnt, num):
  if cnt == k+1:
    answer.append(num)
    return
  
  for i in range(10):
    if visited[i]: continue

    if cnt == 0 or check(num[cnt-1], str(i), signs[cnt-1]):
      visited[i] = 1
      dfs(cnt+1, num+str(i))
      visited[i] = 0

k = int(input())
signs = list(input().split())
visited = [0]*10
answer = []
dfs(0, '')
answer.sort()
print(answer[-1])
print(answer[0])
'''