N = int(input())
sum = 0  # 총점
plus = 0  # 가산점
answer = list(map(int, input().split()))

for i in range(N):
    if answer[i] == 1: 
        plus += 1
        sum += plus
    else:
        plus = 0

print(sum)

# answer[i] 가 1이면 1을 더하고, sum에 plus값을 더해준다
# answer[i] 가 0이면 plus를 1로 초기화한다