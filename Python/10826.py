import sys
read = sys.stdin.readline
d = [0] * 10001
d[1] = 1
N = int(read().rstrip())
for i in range(2, N+1):
    d[i] = d[i-1] + d[i-2]
print(d[N])
