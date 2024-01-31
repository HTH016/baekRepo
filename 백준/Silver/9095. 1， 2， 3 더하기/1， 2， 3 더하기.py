def ott(n): 
    dp = [0] * (n + 4)
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]

test_case = int(input())
for i in range(test_case):
    n = int(input())
    print(ott(n))