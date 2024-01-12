list = []
for i in range(9):
    list.append(int(input()))

max = list[0]
idx = 0
for i in range(1, len(list)):
    if max < list[i]:
        max = list[i]
        idx = i
                 
print(max)
print(idx + 1)      
