n = int(input())
result = 1
i = n
while i > 0:
    result *= i
    i -= 1
    
print( 1 if n == 0 else result ) 