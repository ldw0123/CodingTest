N = int(input())
n = N + 2
ans = 1 * n  # 초기값 설정. 숫자 1이 n번 등장한다는 의미

# 2부터 N까지 순회
for i in range(2, N+1):
    ans += i * n  # 숫자 i가 n번 등장
print(ans)