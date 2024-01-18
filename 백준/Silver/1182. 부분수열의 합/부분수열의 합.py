import sys
from itertools import combinations

input_1 = [int(x) for x in sys.stdin.readline().split()]
int_list = [int(x) for x in sys.stdin.readline().split()]
qnty = input_1[0]
target_sum = input_1[1]
cnt = 0
all_of_combinations = []

for i in range(1, qnty+1):
    all_of_combinations += list(combinations(int_list, i))

for i in range(len(all_of_combinations)):
    if sum(all_of_combinations[i]) == target_sum :
        cnt += 1

print(cnt)