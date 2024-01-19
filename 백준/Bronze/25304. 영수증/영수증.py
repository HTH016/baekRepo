sum = int(input())
num = int(input())
for _ in range(num):
    x, y = map(int, input().split())
    sum -= x * y
print('Yes' if sum == 0 else 'No')    