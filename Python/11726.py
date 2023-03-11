import sys
read = sys.stdin.readline
N = int(read())
d = [0] * (N+2)
d[1] = 1
for i in range(2, N+2):
    d[i] = d[i-1] + d[i-2]
print(d[N+1] % 10007)
