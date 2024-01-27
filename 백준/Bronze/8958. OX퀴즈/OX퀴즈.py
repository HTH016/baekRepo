import sys 

def res(list):
    result, cnt = 0, 0
    if list[0] == 'O':
        cnt = 1
        result = 1
    for i in range(len(list) - 1):
        if list[i + 1] == 'O':
            cnt += 1
        else:
            cnt = 0
        result += cnt
    return result

test_case = int(input())
for _ in range(test_case):
    ox_list = list(sys.stdin.readline())
    print(res(ox_list))    
    