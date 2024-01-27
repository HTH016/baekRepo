n = int(input())
if n < 100:
    print(n)
elif n == 1000:
    print(144)
else:
    cnt = 99
    for i in range(100, n + 1):
        a = i // 100
        b = (i % 100) // 10
        c = i % 10
        if 2 * b == a + c:
            cnt += 1
    print(cnt)        