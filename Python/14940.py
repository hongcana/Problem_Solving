from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().split())
li = []
visited = []
for _ in range(N):
    li.append(list(map(int, read().split())))
    visited.append([0 for _ in range(M)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(pos):
    q = deque()
    q.append(pos)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= N or 0 > ny or ny >= M:
                continue

            elif li[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])


for i in range(N):
    for j in range(M):
        if li[i][j] == 2:
            bfs([i, j])
            visited[i][j] = 0

# li[i][j] == 1인데 visited[i][j] == 0인거 visited -1로 변환
for i in range(N):
    for j in range(M):
        if (li[i][j] == 1) and (visited[i][j] == 0):
            visited[i][j] = -1

for v in visited:
    print(*v)
