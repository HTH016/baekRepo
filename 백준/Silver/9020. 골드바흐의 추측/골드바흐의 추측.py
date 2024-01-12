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
    num_less = int(num/2)
    num_more = int(num/2)
    while(True):
        if is_prime(num_less) and is_prime(num_more):
            break
        num_more += 1
        num_less -= 1 
    return f'{num_less} {num_more}'    

test_case = int(input())
while True:
    try:
        num = int(sys.stdin.readline())
        print(goldbach(num))
    except:
        break
