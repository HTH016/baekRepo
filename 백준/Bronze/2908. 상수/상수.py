def reverse(num):
    num = list(str(num))
    num.reverse()
    num = ''.join(num)
    num = int(num)
    return num

a, b = map(int, input().split())
a = reverse(a)
b = reverse(b)
print(max(a, b))