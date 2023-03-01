# DFS? BFS?
# BFS를 써봅시다.

from collections import deque
import sys
read = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 상 하 좌 우 탐색, row = x // column = y
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0) or (nx >= N) or (ny < 0) or (ny >= M):
                continue

            if nodes[nx][ny] == 0:
                continue

            if nodes[nx][ny] == 1:
                nodes[nx][ny] = 2
                queue.append((nx, ny))


T = int(read())
for _ in range(T):
    M, N, K = map(int, read().split())
    nodes = []
    result = 0
    for i in range(N):
        nodes.append([0 for j in range(M)])

    for _ in range(K):
        x, y = map(int, read().split())
        nodes[y][x] = 1

    for i in range(N):
        for j in range(M):
            # 1인 곳만 bfs
            if nodes[i][j] == 1:
                bfs(i, j)
                result += 1
    print(result)
