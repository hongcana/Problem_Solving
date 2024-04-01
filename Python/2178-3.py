

from collections import deque

N, M = map(int, input().split(" "))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []

for i in range(N):
    graph.append(list(map(int, input())))

# start bfs
queue = deque()
queue.append([0, 0])
while queue:
    x, y = queue.popleft()
    if x == (N-1) and y == (M-1):
        break
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
            queue.append([nx, ny])
            graph[nx][ny] = graph[x][y] + 1

print(graph[N-1][M-1])