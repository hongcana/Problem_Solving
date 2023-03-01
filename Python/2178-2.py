from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().split())

graphs = []

for _ in range(N):
    graphs.append(list(map(int, read().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 다음 방향 테스트
            nx = x + dx[i]
            ny = y + dy[i]

        # 4방향이 미로의 범위를 넘어가는지?
            if (nx < 0) or (nx >= N) or (ny < 0) or (ny >= M):
                continue

        # 벽이니?
            if graphs[nx][ny] == 0:
                continue

        # 첫 방문이니?
            if graphs[nx][ny] == 1:
                graphs[nx][ny] = graphs[x][y] + 1
                queue.append((nx, ny))

    # 첫 지점 거리 계산
    return graphs[N-1][M-1]


print(bfs(0, 0))
