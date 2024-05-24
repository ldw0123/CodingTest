# 시간 초과가 많이 나는 문제이므로, 입력 받을 때 input 대신 stdin.readline()을 써야한다

from sys import stdin

for _ in range(3):
    count = int(stdin.readline())
    list = []
    for _ in range(0, count):
        list.append(int(stdin.readline()))
    if sum(list) > 0:
        print("+")
    elif sum(list) < 0:
        print("-")
    else:
        print(0)