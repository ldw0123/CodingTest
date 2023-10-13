# n: 입력받을 배열의 개수
n = int(input(''))

num = []

for i in range(n):
    A = list(map(int, input('').split()))
    # A리스트에서 가장 큰 값을 2번 반복하여 삭제
    for j in range(2):
        A.remove(max(A))

    # A리스트에서 3번째로 큰 값을 num 배열에 추가
    num.append(max(A))

for i in range(n):
    print(num[i])