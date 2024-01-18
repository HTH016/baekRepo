
def next(num):
    a = num // 10
    b = num % 10 

    return b * 10 + (a + b) % 10

num = int(input())
cnt = 0
comp_num = num
comp_result = 0

while True :
    comp_result = next(comp_num)
    cnt += 1
    if comp_result == num:
        break
    else:
        comp_num = comp_result
print(cnt)