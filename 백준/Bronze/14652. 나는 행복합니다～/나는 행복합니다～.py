# N: 세로 길이, M: 가로 길이, K: 번호

N, M, K = map(int, input().split())

n = K // M  # 세로 위치
m = K % M  # 가로 위치
print(n, m)