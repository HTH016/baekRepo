n, k = list(map(int, input().split(' ')))
cnt = 0
lis = []
for i in range(1, n + 1):
    if i % 10 == k % 10 or i % 10 == 2 * k % 10 :
        continue
    lis.append(i)
    cnt += 1
print(cnt)    
for i in range(cnt):
    print(lis[i], end=' ')
