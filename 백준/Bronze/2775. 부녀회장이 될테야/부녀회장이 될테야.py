def vila(k, n):
    lst = [i for i in range(n + 1)]
    for i in range(k):
        for j in range(1, n):
            lst[j + 1] += lst[j]
    return lst[n]

test_case = int(input())
for i in range(test_case):
    k = int(input())
    n = int(input())
    print(vila(k, n))