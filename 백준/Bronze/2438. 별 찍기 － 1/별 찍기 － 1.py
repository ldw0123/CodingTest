star = ""
number = int(input())

# for ~ in range(n) : 0부터 n-1까지 반복
for i in range(number): # 열
  for j in range(i+1): # 행. 1 ~ number까지 반복
    star += "*"
  star += "\n"
print(star)