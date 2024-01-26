import re

s = input()
s_list = re.split('([-|+])', s)

num_list = []
op_list = []
for strr in s_list:
    if strr == '+' or strr == '-':
        op_list.append(strr)
    else:
        num_list.append(strr)

num_list = list(map(int, num_list))

# print(num_list)
# print(op_list)

op_counter = 0
sum = 0 
sig = 1
for i in op_list:
    op_counter += 1
    if i == '-':
        sig = 0
        break
for i in range(len(num_list)):
    if i < (op_counter + sig):
        sum += num_list[i]
    else:
        sum += num_list[i] * (-1)
print(sum)   
