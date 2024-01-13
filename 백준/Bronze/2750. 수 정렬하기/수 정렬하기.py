import sys
num = int(input())
num_list = [None] * num
for i in range(num):
    num_list[i] = int(input())
for i in range (num - 1):
    for j in range (num - 1):
        if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
for i in range(len(num_list)):
    print(num_list[i])
