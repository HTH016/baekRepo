def tile_2xn_2(n): 
    memo = [0] * (n + 3)
    memo[1], memo[2] = 1, 3
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] * 2
    return memo[n]

n = int(input())
print(tile_2xn_2(n) % 10007)
