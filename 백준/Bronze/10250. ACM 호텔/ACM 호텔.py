test_case = int(input())
for i in range(test_case):
    h, w, n = map(int, input().split())
    print(100 * ((n - 1) % h + 1) +  (n - 1) // h + 1)