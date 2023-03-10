from collections import deque
import sys
read = sys.stdin.readline

N = int(read())
node = []
visited = []

for _ in range(N):
    node.append(list(map(str, read().rstrip())))
    visited.append([0 for _ in range(N)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(pos):
    q = deque()
    q.append(pos)
    visited[pos[0]][pos[1]] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        word = node[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            elif node[nx][ny] == word and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return cnt


count_1 = 0
# 오리지널
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count_1 += bfs((i, j))

for i in range(N):
    for j in range(N):
        if node[i][j] == 'R':
            node[i][j] = 'G'

visited = [[0] * N for _ in range(N)]

count_2 = 0
# 색맹 버전
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count_2 += bfs((i, j))

print(count_1, count_2)
