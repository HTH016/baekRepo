import sys

str_num = int(input())
str_list = [0] * (str_num + 1)
dp_table = [0] * (str_num + 1)
for i in range(1, str_num+1):
    str_list[i] = int(sys.stdin.readline())

# dp 에 n = 3 까지 넣기 
dp_table[1] = str_list[1]
if str_num >= 2: 
    dp_table[2] = str_list[1] + str_list[2]
if str_num >= 3:
    dp_table[3] = str_list[3] + max(str_list[1], str_list[2])
# dp 4부터 넣기 

    for i in range(4, str_num+1):
        dp_table[i] = max(dp_table[i - 3] + str_list[i - 1] + str_list[i], dp_table[i - 2] + str_list[i])

print(dp_table[str_num])
