remain_list = []
rem_knd, price = map(int, input().split())

for i in range(rem_knd):
    remain_list.append(int(input()))
result = 0

remain_list.reverse()
for r in remain_list:
    result += price // r
    price %= r
    if price == 0:
        break

print(result)