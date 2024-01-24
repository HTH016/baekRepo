import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

num_v, num_e = map(int, sys.stdin.readline().split())
edge_list = []
parent = [i for i in range(num_v+1)]

result = 0

for i in range(num_e):
    n_1, n_2, weight = map(int, sys.stdin.readline().split())
    edge_list.append([n_1, n_2, weight])
#print(edge_list)

edge_list.sort(key = lambda x : x[2])
#print(edge_list)

# cnt = 0

for edge in edge_list:
    if find(edge[0]) != find(edge[1]):
        union(edge[0], edge[1])
        # cnt += 1
        result += edge[2]
    # if cnt >= num_v - 1:
    #     break
    # print(cnt)
    
print(result)