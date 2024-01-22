import sys
test_num = int(input())
for _ in range(test_num):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)