s_1, s_2 = input().split()
s_1 = list(s_1)
s_2 = list(s_2)
diff = abs(len(s_1) - len(s_2))
if len(s_1) < len(s_2):
    s_1 = ['0'] * diff + s_1 
elif len(s_2) < len(s_1):
    s_2 = ['0'] * diff + s_2
else:
    pass

cnt = 0
for i in range(len(s_1)):
    if s_1[i] == '8' and s_2[i] == '8':
        cnt += 1
    elif s_1[i] == s_2[i]:
        continue
    else:
        break

print(cnt)