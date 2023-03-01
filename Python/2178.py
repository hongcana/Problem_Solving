import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())

nodes = []
for _ in range(N):
    nodes.append(list(map(int, read().rstrip())))

print(nodes)

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    # initialize queue:
    queue = deque()
    queue.append([x, y])
    # queue가 빌때 까지 반복
    while queue:
        # 현재 위치에서 4가지 방향으로의 위치를 확인
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어난 경우, 무시
            if (nx < 0) or (nx >= N) or (ny >= M) or (ny < 0):
                continue

        # 벽인 경우, 무시
            if nodes[nx][ny] == 0:
                continue

        # 해당 노드를 처음 방문하는 경우에만 최단거리 기록(hint = 0, 1)
            if nodes[nx][ny] == 1:
                nodes[nx][ny] = nodes[x][y] + 1
                queue.append((nx, ny))

        # 가장 오른쪽 구석의 최단거리 반환
    return nodes[N-1][M-1]


print(bfs(0, 0))
