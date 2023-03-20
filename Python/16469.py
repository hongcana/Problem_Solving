from collections import deque
import sys
read = sys.stdin.readline
R, C = map(int, read().split())
li = [list(map(int, read().rstrip())) for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

nuck = list(map(int, read().split()))
nuck[0] -= 1
nuck[1] -= 1
swings = list(map(int, read().split()))
swings[0] -= 1
swings[1] -= 1
chang = list(map(int, read().split()))
chang[0] -= 1
chang[1] -= 1


def bfs(pos, visit):
    q = deque()
    q.append(pos)
    visit[pos[0]][pos[1]] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and li[nx][ny] == 0 and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                q.append([nx, ny])


visited1 = [[-1] * C for _ in range(R)]
bfs(nuck, visited1)
visited2 = [[-1] * C for _ in range(R)]
bfs(swings, visited2)
visited3 = [[-1] * C for _ in range(R)]
bfs(chang, visited3)

score = [[0] * C for _ in range(R)]
for i in range(0, R):
    for j in range(0, C):
        if visited1[i][j] != -1 and visited2[i][j] != -1 and visited3[i][j] != -1:
            score[i][j] = max(visited1[i][j], visited2[i][j], visited3[i][j])

min_val = 1000
cnt = 0
pos_r, pos_c = 0, 0

for i in range(R):
    for j in range(C):
        if score[i][j] > 0:
            if min_val > score[i][j]:
                pos_r = i
                pos_c = j
                min_val = score[i][j]
                cnt = 1
            elif min_val == score[i][j]:
                cnt += 1

if min_val == 1000:
    print(-1)
else:
    print(score[pos_r][pos_c])
    print(cnt)
