# 9x9 table을 생성
table = []
for _ in range(9):
    row = list(map(int, input().split()))
    table.append(row)

# 가장 큰 수와 그것의 위치를 검색
max_num = 0
max_row, max_col = 0, 0

for row in range(9):
    for col in range(9):
        if max_num <= table[row][col]:
            max_row, max_col = row + 1, col + 1
            max_num = table[row][col]

# 가장 큰 수와 위치를 출력
print(max_num)
print(max_row, max_col)