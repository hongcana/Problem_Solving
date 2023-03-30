from collections import deque
import sys
read = sys.stdin.readline
C, R = map(int, read().split())
li = []
visited = []

# 육각형의 벽 개수
value = []
for _ in range(R):
    li.append(list(map(int, read().split())))
    visited.append([-1 for _ in range(C)])
    value.append([0 for _ in range(C)])

# 여섯 방향 좌표, 시계방향으로 1시부터 ~ 11시까지
# 좌표 경우의 수

# 홀수행
dx1 = [-1, 0, 1, 1, 0, -1]
dy1 = [1, 1, 1, 0, -1, 0]

# 짝수행
dx2 = [-1, 0, 1, 1, 0, -1]
dy2 = [0, 1, 0, -1, -1, -1]

# 홀수 행일때, 아래쪽에 있는 좌표는 행만 더해준다.
# 짝수 행일때, 오른쪽 아래에 있는 좌표는 행만 더해준다.
# bfs 돌리기


def bfs(pos):
    # 시작 지점이 회색 벽이라면
    if li[pos[0]][pos[1]] == 1:
        q = deque()
        q.append(pos)
        visited[pos[0]][pos[1]] = 1
        while q:
            x, y = q.popleft()
            value[x][y] = 6
            # 홀수행, 짝수행 여부 결정

            # 홀수면
            if x % 2 == 1:
                for i in range(6):
                    nx = x + dx1[i]
                    ny = y + dy1[i]

                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        continue

                    elif li[nx][ny] == 1 and visited[nx][ny] == -1:
                        visited[nx][ny] = 1
                        value[x][y] -= 1
                        q.append([nx, ny])
            else:
                for i in range(6):
                    nx = x + dx2[i]
                    ny = y + dy2[i]

                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        continue

                    elif li[nx][ny] == 1 and visited[nx][ny] == -1:
                        visited[nx][ny] = 1
                        value[x][y] -= 1
                        q.append([nx, ny])

    # 시작 지점이 흰색 벽이라면
    else:
        grey = 0
        x, y = pos
        # 홀수면
        if x % 2 == 1:
            for i in range(6):
                nx = x + dx1[i]
                ny = y + dy1[i]

                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue

                elif li[nx][ny] == 1:
                    grey += 1

            if grey == 6:
                for i in range(6):
                    nx = x + dx1[i]
                    ny = y + dy1[i]
                    value[nx][ny] -= 1
        else:
            for i in range(6):
                nx = x + dx2[i]
                ny = y + dy2[i]

                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue

                elif li[nx][ny] == 1:
                    grey += 1

            if grey == 6:
                for i in range(6):
                    nx = x + dx2[i]
                    ny = y + dy2[i]
                    value[nx][ny] -= 1


for i in range(R):
    for j in range(C):
        if visited[i][j] == -1:
            bfs([i, j])

# 모든 좌표에 대해서 bfs를 돌리고,
# 만약 6방향 다 탐색했는데 다 회색 벽이다?
# 6방향 회색 벽에 cnt - 1씩 해버리기.

print(value)
