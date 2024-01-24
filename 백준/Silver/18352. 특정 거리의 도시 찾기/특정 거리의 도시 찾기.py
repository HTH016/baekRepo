import sys                              # 빠른 입력을 위한 readline 사용
from collections import deque           # 빠른 알고리즘 연산을 위한 deque 사용

num_city, num_road, target_dist, initial_city = map(int, sys.stdin.readline().split())
INF = 1e9

cnt = 0
visited = [False] * (num_city+1)
dist_table = [0] * (num_city+1)

# 인접 리스트 생성
graph_adj_list = {}
for i in range(num_city):
    graph_adj_list[i + 1] = []

for i in range(num_road): 
    st, ed = map(int, sys.stdin.readline().split())
    graph_adj_list[st].append(ed)

# print(graph_adj_list)

def bfs_adj_lst (init_v):
    queue = deque()
    queue.append(init_v)
    visited[init_v] = True
    while queue:
        v = queue.popleft()
        for i in graph_adj_list[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                dist_table[i] = dist_table[v] + 1
    return visited

bfs_adj_lst(initial_city)
# print(dist_table)


for city in range(1, num_city+1):
    if dist_table[city] == target_dist:
        print(city)
        cnt += 1
if cnt == 0:
    print(-1)
