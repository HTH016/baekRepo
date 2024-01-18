import sys

"""
    정사각형 입력 받는다. 
    숫자 1개일 때 처리
    첫 번째 추출
    if 하나라도 다르면
        4개 분할하여 리턴
    전부 같으면
"""
        

def quad_tree(row, col, size):
    if size == 1:
        print(disp[row][col], end='')
        return 
    first_val = disp[row][col]

    for i in range(row, row + size):
        for j in range(col, col + size):
            if first_val != disp[i][j]:
                print('(', end='')
                size //= 2
                quad_tree(row, col, size)
                quad_tree(row, col + size, size)
                quad_tree(row + size, col, size)
                quad_tree(row + size, col + size, size)
                print(')', end='')
                return
    
    print(disp[row][col], end='')
    return

size = int(input())
disp = [ list(map(int, sys.stdin.readline().strip())) for _ in range(size)]

quad_tree(0, 0, size)


    

