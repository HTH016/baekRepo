import sys

prime_list = []

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def goldbach(num):
    list = [0, 0]

    for i in range((int(num/2)), 1, -1):
        if is_prime(i) and is_prime(num - i):
            list = [i, num - i]
            break
    return list

test_case = int(input())
while True:
    try:
        num = int(sys.stdin.readline())
        print(f'{goldbach(num)[0]} {goldbach(num)[1]}')
    except:
        break
