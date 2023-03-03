from collections import deque
import sys
read = sys.stdin.readline

M, N, H = map(int, read().split())

box = []
for h in range(H):
    box.append(list())
    for i in range(N):
        box[h].append(list(map(int, read().split())))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(visited):
    while visited:
        z, x, y = visited.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                visited.append((nz, nx, ny))


visited = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                visited.append((i, j, k))

while visited:
    bfs(visited)

high = max(box[0][0])
trg = 0

for b in box:
    for j in b:
        if 0 in j:
            print(-1)
            trg = 1
            break
        else:
            if high < max(j):
                high = max(j)
    if trg == 1:
        break

if trg == 0:
    print(high-1)
