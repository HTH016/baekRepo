conf = int(input())
conf_list = []
count_list = []
for i in range(conf):
    st, ed = map(int, input().split())
    conf_list.append([st, ed])

conf_list = sorted(conf_list, key = lambda x: [x[1], x[0]])
pivot = conf_list[0]
cnt = 1
for i in range(conf - 1):
    if pivot[1] <= conf_list[i + 1][0]:
        cnt += 1
        #print(f'cnt = {cnt}')
        pivot = conf_list[i + 1]
    count_list.append(cnt)

print(max(count_list))            
        