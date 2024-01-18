list = [int(x) for x in input().split()]

temp = (60*list[0]+list[1]-45)%1440
print(f'{temp//60} {temp%60}')