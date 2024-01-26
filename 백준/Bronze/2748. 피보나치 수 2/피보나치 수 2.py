memo = [0] * 100
def fibo_dp_td(n):
    if n == 1 or n == 2 :
        return 1
    if memo[n] != 0:
        return memo[n] 
    memo[n] = fibo_dp_td(n - 1) + fibo_dp_td(n - 2)
    return memo[n]

n = int(input())
print(fibo_dp_td(n))