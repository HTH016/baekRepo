def prime(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1        
    return cnt    

n = int(input())
num_list = list(map(int, input().split(' ')))
cnt = 0
for i in range(len(num_list)):
    if prime(num_list[i]) == 2:
        cnt += 1
print(cnt)