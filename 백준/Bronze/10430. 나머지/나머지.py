# 세 수를 입력받는다
A,B,C = input().split()

# int로 형변환
A = int(A) 
B = int(B)
C = int(C)

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)