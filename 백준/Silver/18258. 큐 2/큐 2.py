import sys
front = 0
back = 0

comm_num = int(sys.stdin.readline())
que = []  

for i in range(comm_num):
    command = sys.stdin.readline()
    if command == 'empty\n':
        print(0 if back - front > 0 else 1)
    elif command == 'pop\n':
        if front < back:
            print(que[front])
            front += 1
        else:
            print(-1)
    elif command == 'size\n':
        print(back - front)
    elif command == 'front\n':
        if back - front > 0:
            print(que[front])
        else:
            print(-1)
    elif command == 'back\n':
        if back - front > 0:
            print(que[back-1])
        else:
            print(-1)
    else:
        val = int(command.split(' ')[1])
        # append[ptr] = val
        que.append(val)
        back += 1
    

