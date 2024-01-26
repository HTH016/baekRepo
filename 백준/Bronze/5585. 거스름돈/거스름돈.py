
price = int(input())
remain = 1000 - price
remain_list = [500, 100, 50, 10, 5, 1]
result = 0

for r in remain_list:
    while remain >= r:
        remain -= r
        result += 1
    if remain == 0:
        break

print(result)