# dynamic programming - pibo
# 바텀업
import sys
read = sys.stdin.readline
N = int(read())
tc = [int(read().rstrip()) for _ in range(N)]
f = [0 for _ in range(41)]
f[1] = 1
for i in range(2, 41):
    f[i] = f[i-2] + f[i-1]
for t in tc:
    if t == 0:
        print("1 0")
    else:
        print(str(f[t-1]) + " " + str(f[t]))
