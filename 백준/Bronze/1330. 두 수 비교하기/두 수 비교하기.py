compare = [int(x) for x in input().split()]

if compare[0] > compare[1]:
    print('>')
elif compare[0] < compare[1]:
    print('<')
else:
    print('==')