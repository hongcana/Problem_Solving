import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = [list(map(int, read().split())) for _ in range(N)]
ans = [0, 0]


def recur(r, c, N):
    start = li[r][c]
    for i in range(r, r+N):
        for j in range(c, c+N):
            if li[i][j] != start:
                # 분할
                recur(r, c + N//2, N//2)  # 1
                recur(r, c, N//2)  # 2
                recur(r + N//2, c, N//2)  # 3
                recur(r+N//2, c+N//2, N//2)  # 4
                return 0
    if start == 1:
        ans[1] += 1
    else:
        ans[0] += 1


recur(0, 0, N)
for a in ans:
    print(a)
