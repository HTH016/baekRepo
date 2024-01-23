import sys
from collections import deque

num_v = int(input())
result = [0] * (num_v + 1)
conn_dict = {}

for i in range(num_v):
    conn_dict[i + 1] = []
for i in range(num_v - 1) : 
    n_1, n_2 = map(int, sys.stdin.readline().split())
    conn_dict[n_1].append(n_2)
    conn_dict[n_2].append(n_1)


temp = deque()
temp.append(1)

def find_parent():
    while temp:
        v = temp.popleft()
        for adj in conn_dict[v]:
            if result[adj] == 0:
                result[adj] = v
                temp.append(adj)

find_parent()
result = result[2:]
for c in result:
    print(c)