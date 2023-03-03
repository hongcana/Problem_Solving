from collections import deque
import sys
read = sys.stdin.readline

# BFS

R, C, N = map(int, read().split())
nodes = []
for i in range(R):
    nodes.append(list(map(str, read().rstrip())))
    for j in range(C):
        if nodes[i][j] == 'O':
            nodes[i][j] = 1
        elif nodes[i][j] == '.':
            nodes[i][j] = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(nodes, pos):
    x, y = pos
    nodes[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue

        if nodes[nx][ny] == 3:
            continue

        else:
            nodes[nx][ny] = -1


cnt = 1
while cnt < N:
    # 폭탄심는 반복문
    for i in range(R):
        for j in range(C):
            nodes[i][j] += 1

    # 터뜨리는 반복문
    for i in range(R):
        for j in range(C):
            if nodes[i][j] == 3:
                bfs(nodes, (i, j))
    cnt += 1

for i in nodes:
    for j in range(len(i)):
        if i[j] >= 0:
            i[j] = 'O'
        else:
            i[j] = '.'

for n in nodes:
    print(''.join(n))
