# 시 A, 분 B, 초 C, 필요 시간 D
H, M, S = map(int, input().split())
D = int(input())

S += D
M += S // 60
H += M // 60

S %= 60
M %= 60
H %= 24

print(H, M, S)