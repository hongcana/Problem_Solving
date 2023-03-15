# DP, 1932
import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = [list(map(int, read().split())) for _ in range(N)]
if N == 1:
    print(li[0][0])
elif N == 2:
    print(max(li[1][0]+li[0][0], li[1][1]+li[0][0]))
else:
    li[1][0] += li[0][0]
    li[1][1] += li[0][0]
    for i in range(2, N):
        li[i][0] += li[i-1][0]
        for j in range(1, len(li[i])-1):
            li[i][j] += max(li[i-1][j-1], li[i-1][j])
        li[i][-1] += li[i-1][-1]
    print(max(li[N-1]))
