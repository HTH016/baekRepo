import sys
from collections import deque

std_num, dirc = map(int, sys.stdin.readline().split())
dirc_dict = {}
node_in = [0] * (std_num + 1)
for i in range(std_num + 1):
    dirc_dict[i] = []
for _ in range(dirc) : 
    n_1, n_2 = map(int, sys.stdin.readline().split())
    dirc_dict[n_1].append(n_2)
    node_in[n_2] += 1 
result = []    
# for i in range(comp):
#     front, back = map(int, sys.stdin.readline().split())
#     dirc_dict[i] = [front, back]
#     node_in[back - 1] += 1 
queue = deque()
topol_sort = []
# print(dirc_dict)
# print(node_in)

for i in range(1, std_num+1):
    if node_in[i] == 0:
        queue.append(i)

# print(queue)


while queue:
    std_now = queue.popleft()
    result.append(std_now)
    for adj in dirc_dict[std_now] : 
        node_in[adj] -= 1
        if node_in[adj] == 0:
            queue.append(adj)

# print(result) 

for x in result:
    print(x, end=' ')       
