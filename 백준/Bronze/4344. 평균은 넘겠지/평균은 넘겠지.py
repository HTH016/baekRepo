import sys

def get_sup(list):
    list = list[1:]
    cnt = 0
    avg = sum(list) / len(list)
    for sc in list:
        if sc > avg:
           cnt += 1 
    return cnt 

test_case = int(input())
for _ in range(test_case):
    score_list = list(map(int, sys.stdin.readline().split()))
    ratio = get_sup(score_list) / (len(score_list) - 1) * 100
    print("{:.3f}%".format(ratio))
    
    
