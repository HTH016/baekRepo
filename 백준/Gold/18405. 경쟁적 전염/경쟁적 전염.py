import sys
from collections import deque

size, vir_num = map(int, input().split())
lab = [list(map(int, sys.stdin.readline().split())) for i in range(size)]
sec, t_x, t_y = map(int, sys.stdin.readline().split())
virus_list = []
v_pos_list = []
t_x -= 1
t_y -= 1

for i in range(size):
    for j in range(size):
        if lab[i][j] != 0:
            virus_list.append(lab[i][j])
            v_pos_list.append([lab[i][j], ((abs(i - t_x) + abs(j - t_y)))])
virus_list.sort()

v_pos_list = sorted(v_pos_list, key = lambda x: [-x[1], -x[0]])
if sec < v_pos_list[-1][1]:
    print(0)
else:
    print(v_pos_list[-1][0])
