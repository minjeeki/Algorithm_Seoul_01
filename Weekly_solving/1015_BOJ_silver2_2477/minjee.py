# 참외 개수
K = int(input())
list_len = []

# 가장 큰 면적의 가로와 세로 구하기
max_width = 0
max_height = 0
for i in range(6):
    list_len.append(list(map(int, input().split())))
    if list_len[i][0] in {1, 2}:
        max_width = max(max_width, list_len[i][1])
    elif list_len[i][0] in {3, 4}:
        max_height = max(max_height, list_len[i][1])
# 시작점과 끝점이 가장 큰 가로 또는 세로일 경우를 방지에 이어 붙임
list_len += list_len

minus_width = 0
minus_height = 0

# 가장 큰 가로와 세로의 양 옆의 값은 빼는 길이가 아니다
for idx in range(1, 11):
    if list_len[idx][1] == max_width and list_len[idx][0] in {1, 2}:
        # 양 옆의 값 중 큰 값에서 작은 값 빼면 제외할 부분의 가로 영역
        minus_width = max(list_len[idx - 1][1], list_len[idx + 1][1]) - min(list_len[idx - 1][1], list_len[idx + 1][1])
    if list_len[idx][1] == max_height and list_len[idx][0] in {3, 4}:
        # 양 옆의 값 중 큰 값에서 작은 값 빼면 제외할 부분의 세로 영역
        minus_height = max(list_len[idx - 1][1], list_len[idx + 1][1]) - min(list_len[idx - 1][1], list_len[idx + 1][1])
    # for문 조금이라도 덜 돌기 위해서 값 둘 다 찾으면 종료
    if minus_width != 0 and minus_height != 0:
        break

# 면적 = 가장 큰 값들의 넓이 - 제외할 값들의 넓이
# 우리가 구해야 하는 것은 참외의 개수니까 넓이 차에서 K 곱하기
print(((max_height * max_width) - (minus_height * minus_width)) * K)


'''타입 힌팅 적용하기
from typing import List, Tuple

K: int = int(input())

list_len: List[Tuple[int, int]] = []

max_width: int = 0
max_height: int = 0

for i in range(6):
    direction, length = map(int, input().split())
    list_len.append((direction, length))
    if direction in {1, 2}:  # 가로 (동, 서)
        max_width = max(max_width, length)
    elif direction in {3, 4}:  # 세로 (남, 북)
        max_height = max(max_height, length)

list_len += list_len

minus_width: int = 0
minus_height: int = 0

for idx in range(1, 11):
    if list_len[idx][1] == max_width and list_len[idx][0] in {1, 2}:
        minus_width = max(list_len[idx - 1][1], list_len[idx + 1][1]) - min(list_len[idx - 1][1], list_len[idx + 1][1])
    if list_len[idx][1] == max_height and list_len[idx][0] in {3, 4}:
        minus_height = max(list_len[idx - 1][1], list_len[idx + 1][1]) - min(list_len[idx - 1][1], list_len[idx + 1][1])
    if minus_width != 0 and minus_height != 0:
        break
result: int = ((max_height * max_width) - (minus_height * minus_width)) * K
print(result)


# 타입 힌팅 (Type Hinting)
: 변수, 함수의 매개변수, 반환 값에 대해 예상되는 데이터 타입을 명시적으로 표기하는 것
- 파이썬은 동적 타이핑 (dynamic typing) 언어이기 때문에 변수를 선언할 때 데이터 타입을 지정하지 않음
- 타입 힌팅을 통해 명시적으로 타입을 표현할 수 있음 (동적 타이핑을 제한하지 않으면서 타입 정보를 추가적으로 제공)
    => 정적 언어처럼 미리 타입을 강제하는 것은 아니지만 코드의 품질을 높이기 위한 힌트로 사용됨

## 타입 힌팅을 사용하는 이유
- 코드 가독성 향상 : 코드에 데이터 타입을 명시하면 코드 작성자나 읽는 사람이 변수가 어떤 타입인지 쉽게 이해 가능
- 명확한 의도 표현 : 함수의 매개변수와 반환타입을 명확시 지정해, 함수의 사용 방법을 더 직관적으로 알 수 있음
- IDE 및 린터 지원 : IDE나 린터가 코드를 검사할 때 타입 관련 오류를 미리 감지해 경고를 줄 수 있음
    => 타입 관련 버그를 사전에 방지할 수 있음
- 유지 보수 용이 : 여러명이 협력하는 경우 변수나 함수의 타입이 명시되어 있으면, 그 의도를 쉽게 이해할 수 있고 코드 수정 또는 확장 시 관련 실수를 줄일 수 있음
'''