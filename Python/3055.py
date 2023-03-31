from collections import deque
import sys
read = sys.stdin.readline

R, C = map(int, read().split())
li = []
for _ in range(R):
    li.append(list(map(str, read().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs_water(pos):
    q = deque()
    q.append(pos)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and ((li[nx][ny] == '.') or (li[nx][ny] == 'S')):
                water.append([nx, ny])


def bfs_dochi(pos):
    q = deque()
    q.append(pos)
    go = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and li[nx][ny] != 'X':
                dochimove.append([nx, ny])


dochi_cnt = 0
trg = 1
while trg:
    water = deque()
    dochimove = deque()

    for i in range(R):
        for j in range(C):
            if li[i][j] == '*':
                bfs_water([i, j])

    for i in range(R):
        for j in range(C):
            if li[i][j] == 'S':
                bfs_dochi([i, j])

    while water:
        x, y = water.popleft()
        li[x][y] = '*'

    change = 0
    dochi_cnt += 1
    while dochimove:
        x, y = dochimove.popleft()
        if li[x][y] == 'D':
            print(dochi_cnt)
            change = 1
            trg = 0
            break
        elif li[x][y] != '*':
            li[x][y] = 'S'
            change = 1

    if change == 0:
        print("KAKTUS")
        trg = 0
