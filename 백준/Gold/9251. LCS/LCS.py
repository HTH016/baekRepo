
str_1 = list(input())
str_2 = list(input())

len_1 = len(str_1)
len_2 = len(str_2)

table = [[0] * (len_2 + 1) for _ in range(len_1 + 1)]

for i in range(1, len_1 + 1):
    for j in range(1, len_2 + 1):
        if str_1[i - 1] == str_2[j - 1]:
            table[i][j] = table[i - 1][j - 1] + 1 
        else:
            table[i][j] = max(table[i - 1][j], table[i][j - 1])
print(table[-1][-1])