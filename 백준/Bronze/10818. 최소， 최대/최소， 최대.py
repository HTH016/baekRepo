import sys

n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))

max = -1e8
min = 1e8
for i in n_list:
    if i < min:
        min = i
    if i > max:
        max = i

print(f'{min} {max}')