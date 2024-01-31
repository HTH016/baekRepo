
x, y = input().split()
x_1 = x.replace('5', '6')
x_2 = x.replace('6', '5')
y_1 = y.replace('5', '6')
y_2 = y.replace('6', '5')
print(f'{int(x_2)+int(y_2)} {int(x_1)+int(y_1)}')
