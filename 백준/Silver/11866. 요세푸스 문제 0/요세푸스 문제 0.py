
input_1 = list(map(int, input().split()))
qnty = int(input_1[0])

num_list = list(range(1, qnty+1))

gap = int(input_1[1])

result = [None] * qnty

for i in range (qnty):
    for j in range (gap - 1):
        num_list.append(num_list[0])
        num_list = num_list[1:]
    result[i] = num_list[0] 
    num_list = num_list[1:]

ans = ''
for i in range (qnty):
    ans += str(result[i]) + ', '
ans = '<'+ ans[:-2] + '>'
print(ans)