import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(read().rstrip())
li = []
dp = []
for _ in range(N):
    li.append(list(map(int, read().split())))
    dp.append([-1 for _ in range(N)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(pos):
    x, y = pos
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue

        if li[x][y] < li[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs([nx, ny])+1)

    return dp[x][y]


maxi = -1
for i in range(N):
    for j in range(N):
        maxi = max(maxi, dfs([i, j]))

print(dp)
print(maxi)
