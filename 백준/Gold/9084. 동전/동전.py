import sys

def case_count(coin_list, total_price):
    dp_table = [1] * (total_price + 1)
    for i in range(len(dp_table)):
        if i % coin_list[0] != 0:
            dp_table[i] = 0
    for i in range(1, len(coin_list)):
        for j in range(len(dp_table)):
            if j >= coin_list[i]:
                dp_table[j] += dp_table[j - coin_list[i]]
    print(dp_table[-1])            

test_case = int(input())
for i in range(test_case):
    coin_num = int(input())
    coin_list = list(map(int, sys.stdin.readline().split()))
    total_price = int(input())
    case_count(coin_list, total_price)    

