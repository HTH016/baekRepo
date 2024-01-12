import sys

while True:
    try:
        data = list(sys.stdin.readline().split())
        if len(data) == 1:
            continue
        num = int(data[0])
        str = list(data[1])
        for i in range(len(str)):
            print(str[i] * num, end='')
            
        print()
    except:
        break
    