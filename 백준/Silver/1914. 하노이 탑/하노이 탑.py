def move(no: int, start: int, end: int) -> None:
    
    if no > 1:
        move(no - 1, start, 6 - (start + end))
    print(f'{start} {end}')
    if no > 1:
        move(no - 1, 6 - (start + end), end)

n = int(input())

print(2**n - 1)
if n <= 20:
    move(n, 1, 3)
