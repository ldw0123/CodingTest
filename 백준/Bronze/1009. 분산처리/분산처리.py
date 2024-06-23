T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    a %= 10  # 1의 자리의 수를 구한다

    if a == 0:  # a의 1의 자리가 0일 때
        print(10)  # 10번 컴퓨터
    elif a == 1 or a == 5 or a == 6:  # a의 1의 자리가 1, 5, 6일 때
        print(a)
    elif a == 4 or a == 9:  # a의 1의 자리가 4, 9일 때
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:  # b가 4인 경우, b % 4 = 1로 되어 계산하는 것 방지
            print((a**4) % 10 % 10 % 10)
        else:
            print((a**b) % 10 % 10 % 10)