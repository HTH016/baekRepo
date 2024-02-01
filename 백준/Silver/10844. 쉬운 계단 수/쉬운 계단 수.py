
init_list = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
scnd_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def lst_chng(list_1, list_2):
    list_2[0] = list_1[1]
    list_2[-1] = list_1[-2]
    for i in range(1, 9):
        list_2[i] = list_1[i - 1] + list_1[i + 1]

n = int(input())
if n == 1:
    print(9)
else:
    for i in range((n-1)//2):
        lst_chng(init_list, scnd_list)
        lst_chng(scnd_list, init_list)
    if n % 2 == 0:
        lst_chng(init_list, scnd_list)
        print(sum(scnd_list) % 1000000000)
    else:
        print(sum(init_list) % 1000000000)
    