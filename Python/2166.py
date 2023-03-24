# n각형의 넓이 공식
# 1/2 (x1y2 - y1x2 + x2y3 - y2x3 + ... + xny1 - ynx1)
import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = [list(map(int, read().split())) for _ in range(N)]

result = 0
for i in range(0, N):
    if i == (N-1):
        result += (li[i][0] * li[0][1]) - (li[i][1] * li[0][0])
    else:
        result += (li[i][0] * li[i+1][1]) - (li[i][1] * li[i+1][0])

print(abs(round(result/2, 1)))
