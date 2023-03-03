from collections import deque
import sys
read = sys.stdin.readline

M, N = map(int, read().split())

box = []
for i in range(N):
    box.append(list(map(int, read().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(visited):
    while visited:
        x, y = visited.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                visited.append((nx, ny))


visited = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            visited.append((i, j))

while visited:
    bfs(visited)

high = max(box[0])
trg = 0
for b in box:
    if 0 in b:
        print(-1)
        trg = 1
        break
    else:
        if high < max(b):
            high = max(b)

if trg == 0:
    print(high-1)
