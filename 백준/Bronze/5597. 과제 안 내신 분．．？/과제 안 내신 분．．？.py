STD_N = 30
arr = [i for i in range (1, STD_N + 1)]
ar = []
for i in range(STD_N - 2): 
    ar.append(int(input()))
s = list(set(arr) - set(ar))
if s[0] < s[1]:
    print(s[0])
    print(s[1])
else:
    print(s[1])
    print(s[0])