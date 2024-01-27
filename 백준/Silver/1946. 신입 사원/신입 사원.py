import sys
MAX = 1e7

def pass_num(list):
    comp = MAX
    cnt = 0
    for i in list:
        if i < comp: 
            cnt += 1
            comp = i
    return cnt

test_case = int(input())
for _ in range(test_case):
    app_num = int(input())
    app_info = [0] * (app_num + 1)
    for i in range(app_num):
        fst, snd = map(int, sys.stdin.readline().split())
        app_info[fst] = snd
    app_info = app_info[1:]
    print(pass_num(app_info))