import sys
sys.setrecursionlimit(10 ** 9)

pre_ordered = []

def pre_to_post(start, end):
    if start > end:
        return
    idx = end + 1
    for i in range(start+1, end+1):
        if pre_ordered[start] < pre_ordered[i]:
            idx = i
            break   
    pre_to_post(start+1, idx-1)
    pre_to_post(idx, end)
    print(pre_ordered[start])

while True:
    try:
        val = pre_ordered.append(int(sys.stdin.readline()))
    except:
        break

pre_to_post(0, len(pre_ordered)-1)





