T = int(input())

for _ in range(T):
    q = input()
    N = int(input())
    list = [int(input()) for _ in range(N)]
    print("YES" if sum(list) % N == 0 else "NO")