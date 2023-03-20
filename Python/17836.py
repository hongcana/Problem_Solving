import sys
from collections import deque
read = sys.stdin.readline
N, M, T = map(int, read().split())
li = [list(map(int, read().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
gram = 1000000


def bfs(pos):
    global gram
    q = deque()
    q.append(pos)
    visited[pos[0]][pos[1]] = 0

    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            return min(gram, visited[N-1][M-1])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            else:
                # gram이니?
                if li[nx][ny] == 2 and visited[nx][ny] == -1:
                    gram = ((N-1)-nx)+((M-1)-ny) + visited[x][y] + 1
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])

                elif li[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
    if gram != 1000000:
        return gram
    else:
        return -1


result = bfs([0, 0])

if result == -1 or result > T:
    print('Fail')
else:
    print(result)
