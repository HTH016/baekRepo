strs = input().split(' ')
n = len(strs)
if strs[0] == '':
    n -= 1
if strs[-1] == '':
    n -= 1
print(n)
