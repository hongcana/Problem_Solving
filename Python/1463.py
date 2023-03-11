# bottom-up DP
import sys
read = sys.stdin.readline
d = [0] * 1000001
d[2] = 1
d[3] = 1

for i in range(4, 1000001):
    if i % 3 == 0 and i % 2 == 0:
        d[i] = min(1 + d[i//3], 1 + d[i//2], 1 + d[i-1])
    elif i % 3 == 0:
        d[i] = min(1 + d[i//3], 1 + d[i-1])
    elif i % 2 == 0:
        d[i] = min(1 + d[i//2], 1 + d[i-1])
    else:
        d[i] = 1 + d[i-1]

print(d[int(read().rstrip())])
