K = 15746
def fibo_dp_bu(n):
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % K
    return dp[n]

n = int(input())
dp = [0] * 1000002
print(fibo_dp_bu(n + 1))