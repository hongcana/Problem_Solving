# BFS
from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().split())
ice = []

visited = []
for _ in range(N):
    ice.append(list(map(int, read().split())))
    visited.append([0 for _ in range(M)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(pos):
    queue = deque([])
    queue.append(pos)
    del_list = []
    visited[pos[0]][pos[1]] = 1

    while queue:
        x, y = queue.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            elif ice[nx][ny] == 0:
                cnt += 1

            elif ice[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

        if cnt > 0:
            del_list.append((x, y, cnt))

    for x, y, cnt in del_list:
        ice[x][y] = max(0, ice[x][y] - cnt)

    return 1

# del list에 값을 감소시켜야 하는 좌표를 추가 시켜서
# 나중에 queue를 다 돈다음 한꺼번에 감소 시키기

total = 0
group = 0
while True:
    for i in range(1, N-1):
        for j in range(1, M-1):
            if ice[i][j] != 0 and visited[i][j] == 0:
                group += BFS((i, j))

    visited = []
    for _ in range(N):
        visited.append([0 for _ in range(M)])

    if group > 1:
        print(total)
        break

    if group == 0:
        print(0)
        break

    group = 0
    total += 1
