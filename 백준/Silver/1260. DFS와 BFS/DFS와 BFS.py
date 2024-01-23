import sys                              # 빠른 입력을 위한 readline 사용
from collections import deque           # 빠른 알고리즘 연산을 위한 deque 사용

def dfs_recur_adj_lst (v, visited=[]):
    visited.append(v)
    for i in graph_adj_list[v]:
        if i not in visited:    
            visited = dfs_recur_adj_lst(i, visited)
    return visited

def bfs_stck_adj_lst (init_v):
    visited = []
    stack = deque()
    stack.append(init_v)
    while stack:
        v = stack.popleft()
        if v not in visited:
            visited.append(v)
            for w in graph_adj_list[v]:
                stack.append(w)
    return visited

num_v, num_e, init_v = map(int, sys.stdin.readline().split())

graph_adj_list = {}
for i in range(num_v):
    graph_adj_list[i + 1] = []

for i in range(num_e):
    n_1, n_2 = map(int, sys.stdin.readline().split())
    graph_adj_list[n_1].append(n_2)
    graph_adj_list[n_2].append(n_1)

for i in range(num_v):
    graph_adj_list[i + 1].sort()
    
ans_1 = dfs_recur_adj_lst(init_v)
ans_2 = bfs_stck_adj_lst(init_v)

for i in ans_1:
    print(i, end=' ')

print()    
for i in ans_2:
    print(i, end=' ')
