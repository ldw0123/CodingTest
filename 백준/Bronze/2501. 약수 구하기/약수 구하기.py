N, K = map(int, input().split())
list = []

# 1부터 N까지 반복
for i in range(1, N+1):
    if N % i == 0:
        list.append(i)

if len(list) < K:  # 약수의 개수가 K보다 작을 때, 0을 출력
    print(0)
else:
    print(list[K - 1])