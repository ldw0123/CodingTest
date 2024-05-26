M = int(input())
cups = [1, 0, 0]  # 공은 1번 컵에 있음

for i in range(M):
    x, y = map(int, input().split())
    cups[x-1], cups[y-1] = cups[y-1], cups[x-1]

print(cups.index(1) + 1)