while True:
    n = int(input())
    
    if n == 0:
        break
    else:
        s = list(str(n))
        sr = list(reversed(s))
        if s == sr:
            print('yes')
        else:
            print('no')