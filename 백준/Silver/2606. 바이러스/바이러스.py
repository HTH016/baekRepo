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

v = int(input())
e = int(input())
#v, e = map(int, sys.stdin.readline().split())
parent = [i for i in range(v+1)]
become_set = []

for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

for i in range(1, v + 1):
    become_set.append(find(i))

com_1 = become_set[0]
print(become_set.count(com_1) - 1)