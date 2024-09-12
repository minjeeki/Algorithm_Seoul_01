N = int(input())

count_list = [0]*1001 # 미리 경우의 수를 담을 리스트를 만들어주기. 0~1000까지
# 0번 자리까지 맞춰줬으니 인덱스 번호가 구할 번호
count_list[1] = 1
count_list[2] = 2

for i in range(3, N+1): # N번째 인덱스까지 계산하기
    count_list[i] = count_list[i-1] + count_list[i-2]

print(count_list[N]%10007) # N번째 경우의 수를 10007로 나눴을 때 나머지 값 구하기
