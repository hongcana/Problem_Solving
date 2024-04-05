
from collections import deque

N, M = map(int, input().split(" "))

graph = [ list(map(int, input().split(" "))) for _ in range(N)]
visited = [ [0 for _ in range(M)] for _ in range(N)]

dx = [-1, 1,0 ,0]
dy = [0, 0, -1 ,1]

target_n, target_m = 0, 0

# 2찾기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            target_n, target_m = i, j
            break

queue = deque()
queue.append([target_n, target_m])
graph[target_n][target_m] = 0
visited[target_n][target_m]=0
while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        
        # 조건
        # visited[nx][ny] == 0
        # nx < N, ny < M
        # graph[nx][ny] >= 1

        if (0<=nx < N) and (0<=ny < M) and visited[nx][ny] == 0 and graph[nx][ny] >= 1:
            queue.append([nx, ny])
            graph[nx][ny] = graph[x][y] + 1
            visited[nx][ny] = 1

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and graph[i][j] != 0:
            graph[i][j] = -1

for g in graph:
    print(*g)