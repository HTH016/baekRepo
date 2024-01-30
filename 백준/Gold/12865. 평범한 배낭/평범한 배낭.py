import sys

kind, weight = map(int, sys.stdin.readline().split())
weight_list = [0]
value_list = [0]
for i in range(kind):
    w, v = map(int, sys.stdin.readline().split())
    weight_list.append(w)
    value_list.append(v)
    
dp_table = [[0 for _ in range(weight + 1)] for _ in range(kind + 1)]

for i in range(1, kind + 1):
    for j in range(1, weight + 1):
        if j < weight_list[i]:
            dp_table[i][j] = dp_table[i - 1][j]
        else:
            dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i - 1][j - weight_list[i]] + value_list[i])

print(dp_table[-1][-1])