import sys

row_num, col_num = map(int, sys.stdin.readline().split())
maze = [list(map(int, input())) for _ in range(row_num)] 

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find_way(row, col):
    queue = []
    queue.append([row, col])
    while queue:
        row, col = queue[0][0], queue[0][1]
        queue = queue[1 : ]
        for c in range(4):
            if 0 <= row + dy[c] < row_num and 0 <= col + dx[c] < col_num :
                if maze[row + dy[c]][col + dx[c]] == 1:
                    maze[row + dy[c]][col + dx[c]] = maze[row][col]+ 1
                    queue.append([row + dy[c], col + dx[c]])

find_way(0, 0)
print(maze[row_num-1][col_num-1])