import sys

test_num = int(input())
for i in range(test_num):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {a+b}')