numbers = []
sum = 0

for i in range(7):
    n = int(input())
    if (n % 2 == 1):
        numbers.append(n)
        sum += n

if numbers == []:  # 빈 list이면 -1 출력
    print(-1)
else:
    print(sum)
    print(min(numbers))