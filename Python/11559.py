from collections import deque
import sys
read = sys.stdin.readline

puyos = []

for i in range(12):
    puyos.append(list(map(str, read().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(pos):
    queue = deque()
    queue.append(pos)
    stackx = list([pos[0]])
    stacky = list([pos[1]])
    bayoen = 1
    visited[pos[0]][pos[1]] = 1
    while queue:
        x, y = queue.popleft()
        puyo = puyos[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= 12 or 0 > ny or ny >= 6:
                continue

            elif puyos[nx][ny] == puyo and visited[nx][ny] == 0:
                stackx.append(nx)
                stacky.append(ny)
                queue.append((nx, ny))
                visited[nx][ny] = 1
                bayoen += 1
    return bayoen, stackx, stacky


def gravity():
    for c in range(6):
        queue = deque([])
        for r in range(11, -1, -1):
            if puyos[r][c] != '.':
                queue.append(puyos[r][c])

        for r in range(len(queue)):
            puyos[11-r][c] = queue[r]
        for r in range(12-len(queue)):
            puyos[r][c] = '.'


trg = 1
result = 0
while trg > 0:
    trg -= 1
    visited = []
    for _ in range(12):
        visited.append([0, 0, 0, 0, 0, 0])

    for i in range(12):
        for j in range(6):
            if puyos[i][j] != '.' and visited[i][j] == 0:
                bayoen, x, y = bfs((i, j))
                if bayoen >= 4:
                    trg = 1
                    for i in range(len(x)):
                        puyos[x[i]][y[i]] = '.'

    if trg == 1:
        result += 1
    gravity()

print(result)
