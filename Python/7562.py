from collections import deque
import sys
read = sys.stdin.readline

N = int(read().rstrip())
cnt = 0

# 나이트의 이동 범위, 12시부터 시계 방향
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(startx, starty):
    q = deque([])
    q.append([startx, starty, 0])
    while q:
        x, y, cnt = q.popleft()
        if x == end_x and y == end_y:
            return cnt
        else:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < M and 0 <= ny < M and visited[nx][ny] == -1:
                    visited[nx][ny] = 1
                    q.append([nx, ny, cnt+1])


while cnt < N:
    cnt += 1
    M = int(read().rstrip())
    board = [[0 for _ in range(M)] for _ in range(M)]
    visited = [[-1 for _ in range(M)] for _ in range(M)]
    start_x, start_y = map(int, read().split())
    end_x, end_y = map(int, read().split())
    print(bfs(start_x, start_y))
