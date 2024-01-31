while True:
    a, b, c = map(int, input().split())
    if a * b * c == 0:
        break
    else:
        m = max(a, b, c)
        if a*a + b*b + c*c == 2*m*m:
            print('right')
        else:
            print('wrong')