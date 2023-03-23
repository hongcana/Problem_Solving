from collections import deque
import sys
read = sys.stdin.readline
N, L, R = map(int, read().split())
li = [list(map(int, read().split())) for _ in range(N)]
# 방문 여부
visited = [[-1] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(pos):
    q = deque()
    q.append(pos)
    members = []
    sum = 0
    global sub
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        members.append([x, y, li[x][y]])
        sum += li[x][y]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue

            elif (L <= abs(li[x][y] - li[nx][ny]) <= R) and visited[nx][ny] == -1:
                visited[nx][ny] = 1
                sub = max(0, abs(li[x][y] - li[nx][ny]))
                q.append([nx, ny])
    return members, sum, sub


cnt = -1
while True:
    cnt += 1
    sub = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                result, sum, sub = bfs([i, j])
                for r in result:
                    li[r[0]][r[1]] = sum // len(result)

    # 방문 초기화
    visited = [[-1] * N for _ in range(N)]
    if L > sub or sub > R:
        break
print(cnt)
