import sys

row_n, col_n = map(int, sys.stdin.readline().split())
floor = []
for i in range(row_n):
    strr = sys.stdin.readline()
    strr = list(strr)
    floor.append(strr[:-1])

result = row_n * col_n

for row in floor:
    for i in range(col_n - 1):
        if row[i] == '-' and row[i + 1] == '-':
            result -= 1

for i in range(row_n - 1):
    for j in range(col_n):
        if floor[i][j] == '|' and floor[i + 1][j] == '|':
            result -= 1

print(result)


