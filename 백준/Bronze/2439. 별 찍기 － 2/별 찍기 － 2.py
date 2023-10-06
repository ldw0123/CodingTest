number = int(input())

for i in range(1, number+1):  # 1부터 number까지 반복
    print(" " * (number-i) + "*" * i)