num_list = list(map(int, input().split()))
cnt_1 = 0
cnt_2 = 0
for i in range(1, 9):
    if i == num_list[i - 1]:
        cnt_1 += 1
    if i + num_list[i - 1] == 9:
        cnt_2 += 1
    
if cnt_1 == 8:
    print('ascending')
elif cnt_2 == 8:
    print('descending')
else:
    print('mixed')
    