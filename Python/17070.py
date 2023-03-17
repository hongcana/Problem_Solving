import sys
read = sys.stdin.readline
# using DFS
N = int(read().rstrip())
li = [list(map(int, read().split())) for _ in range(N)]


def dfs(x, y, dir):
    global cnt
    if x == N-1 and y == N-1:
        cnt += 1
        return

    # 가로 이동 가능의 경우
    if dir == 0 or dir == 1:
        if y+1 < N and li[x][y+1] == 0:
            dfs(x, y+1, 0)

    # 세로 이동 가능의 경우
    if dir == 1 or dir == 2:
        if x+1 < N and li[x+1][y] == 0:
            dfs(x+1, y, 2)

    # 대각선 이동 가능의 경우
    if x+1 < N and y+1 < N and li[x+1][y+1] == 0 and li[x][y+1] == 0 and li[x+1][y] == 0:
        dfs(x+1, y+1, 1)

cnt = 0
dfs(0, 1, 0)
print(cnt)
