
# 입력
dwf = [None] * 9 
for i in range(9):
    dwf[i] = int(input())
    
# 탐색
sum = sum(dwf)
remains = sum - 100 
idx_1 = 0
idx_2 = 0

for i in range (8):
    for j in range (i + 1, 9):
        if dwf[i] + dwf[j] == remains:
            idx_1, idx_2 = i, j
            break         
dwf.remove(dwf[idx_2])
dwf.remove(dwf[idx_1])

# 정렬 

n = 7
k = 0
while k < n - 1:
    last = n - 1
    for j in range(n-1, k, -1):
        if dwf[j - 1] > dwf[j]:
            dwf[j - 1], dwf[j] = dwf[j], dwf[j - 1]
            last = j
    k = last


# 출력 
for i in range(7):
    print(dwf[i])