# 직사각형에서 탈출 (1085) Bronze III
# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

# min() 함수 : min(iterable) 형태로 사용한다. 요소들을 비교하여 최소값을 반환한다

x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))
