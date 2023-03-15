from collections import deque
import sys
read = sys.stdin.readline
N, M = map(int, read().split())
li = [list(map(int, read().rstrip())) for _ in range(N)]
visited = []
for _ in range(N):
    visited.append([[0] * 2 for _ in range(M)])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(pos):
    q = deque([])
    q.append(pos)
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 안에 있고, 단 한 번도 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][w] == 0:
                # 벽이 아니라면 이동
                if li[nx][ny] == 0:
                    q.append((nx, ny, w))
                    visited[nx][ny][w] = visited[x][y][w] + 1

                # 부수기 찬스 있으면
                if w == 0 and li[nx][ny] == 1:
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][w] + 1
    return -1


print(bfs((0, 0, 0)))
