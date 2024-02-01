def fibo_dp_bu(n):
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


test_case = int(input())

for i in range(test_case):

    n = int(input())
    dp = [0] * (n + 1)
    if n == 0:
        qnty_of_zero, qnty_of_one = 1, 0
    else:
        qnty_of_zero, qnty_of_one = fibo_dp_bu(n - 1), fibo_dp_bu(n)

    print(f'{qnty_of_zero} {qnty_of_one}')