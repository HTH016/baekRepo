x, y, w, h = map(int, input().split())

min_x = x if 2*x < w else w - x
min_y = y if 2*y < h else h - y
min = min_x if min_x < min_y else min_y
print(min)