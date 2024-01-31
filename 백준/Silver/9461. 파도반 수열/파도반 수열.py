
def pdb(n):
    dp_table = [1 for i in range(n + 10)]
    dp_table[4] = 2
    dp_table[5] = 2
    for i in range(6, n + 1):
        dp_table[i] = dp_table[i - 1] + dp_table[i - 5]   
    return dp_table[n]

test_case = int(input())
for i in range(test_case):
    n = int(input())
    print(pdb(n))