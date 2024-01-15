import sys
ptr = 0

comm_num = int(sys.stdin.readline())
stack = [None] * comm_num 

for i in range(comm_num):
    command = sys.stdin.readline()
    if command == 'empty\n':
        print(0 if ptr > 0 else 1)
    elif command == 'pop\n':
        if ptr > 0:
            print(stack[ptr-1])
            ptr -= 1
        else:
            print(-1)
    elif command == 'size\n':
        print(ptr)
    elif command == 'top\n':
        if ptr > 0:
            print(stack[ptr-1])
        else:
            print(-1)
    else:
        val = int(command.split(' ')[1])
        stack[ptr] = val
        ptr += 1
    

