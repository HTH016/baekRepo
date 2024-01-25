import sys
from collections import deque

size = int(input())
land = [list(map(int, input())) for _ in range(size)] 
visited = [[False for _ in range(size)] for _ in range(size)]


# print(land)
# print(visited)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def estimate(init_row, init_col):
    
    queue = deque()
    cnt = 0
    queue.append([init_row, init_col])
    #print(queue)
    land[init_row][init_col] = 0
    cnt += 1
    while queue:
        pos_now = queue.popleft()
        #print(f'현재 위치 : {pos_now}')
        land[init_row][init_col] = 0
        for j in range(4):
            re_pos = [pos_now[0] + dy[j], pos_now[1] + dx[j]]
            if (0 <= re_pos[0] < size and 0 <= re_pos[1] < size and 
                land[re_pos[0]][re_pos[1]] == 1):
                queue.append([re_pos[0], re_pos[1]])
                land[re_pos[0]][re_pos[1]] = 0
                #print(f'큐에 추가 : {[re_pos[0], re_pos[1]]}')
                cnt += 1 
        #print(land)
    return cnt

record = [estimate(i, j) for i in range(size) for j in range(size) if land[i][j] == 1]
record.sort()
print(len(record))
for i in record:
    print(i)
