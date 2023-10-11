while True:
    num = input()
    width = 1
    if num == '0':  # 0을 입력받으면 프로그램 종료
        break
    for i in num:
        if i == '0':  # 0은 4cm를 차지함
            width += 4
        elif i == '1':  # 1은 2cm를 차지함
            width += 2
        else:  # 나머지 수는 3cm를 차지함
            width += 3
    width += len(num)  # num의 자리수 만큼 여백을 더함
    print(width)