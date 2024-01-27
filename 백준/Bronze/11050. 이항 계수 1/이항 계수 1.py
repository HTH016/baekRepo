n, k = map(int, input().split())
mult = 1
dp = [1]
for i in range(1, 11):
    mult *= i
    dp.append(mult)

print(dp[n] // (dp[n - k] * dp[k]))