import sys

qnty = int(input())
dp_table = [1] * qnty
num_list = list(map(int, sys.stdin.readline().split()))

for i in range(1, qnty):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)
print(max(dp_table))
