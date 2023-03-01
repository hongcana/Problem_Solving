# using BFS
from collections import deque
import sys
read = sys.stdin.readline
N = int(read())

nodes = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    queue = deque()
    queue.append((x, y))
    count = 0
    nodes[x][y] = 0
    while queue:
        x, y = queue.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0) or (nx >= N) or (ny < 0) or (ny >= N):
                continue

            # 미로찾기 같은 방식이 아니라 없어도 될듯
            # if nodes[nx][ny] == 0:
            #     continue

            if nodes[nx][ny] == 1:
                queue.append((nx, ny))
                nodes[nx][ny] = 0

    return count


for _ in range(N):
    nodes.append(list(map(int, read().rstrip())))

li = []
cnt = 0
for a in range(N):
    for b in range(N):
        if nodes[a][b] == 1:
            cnt += 1
            li.append(dfs(a, b))

print(cnt)
li.sort()
for i in li:
    print(i)
