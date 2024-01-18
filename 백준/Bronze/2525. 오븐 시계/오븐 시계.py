list = [int(x) for x in input().split()]
interval = int(input())

temp = (60*list[0]+list[1] + interval) % 1440
print(f'{temp//60} {temp%60}')