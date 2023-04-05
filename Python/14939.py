import sys
import copy
read = sys.stdin.readline
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]
li = [[False for _ in range(10)] for _ in range(10)]

for i in range(10):
    tmp = list(map(str, read().rstrip()))
    for j in range(10):
        if tmp[j] == 'O':
            li[i][j] = True


def off(b, x, y):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10:
            b[nx][ny] = not b[nx][ny]


ans = 101
for i in range(1 << 10):
    board = copy.deepcopy(li)
    cnt = 0
    for j in range(10):
        if i & (1 << j):
            cnt += 1
            off(board, 0, j)

    for j in range(1, 10):
        for k in range(10):
            if board[j-1][k]:
                cnt += 1
                off(board, j, k)

    if not any(board[9]):
        ans = min(ans, cnt)

print(ans if ans != 101 else -1)
