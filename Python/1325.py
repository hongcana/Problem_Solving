from collections import deque
import sys
read = sys.stdin.readline
N, M = map(int, read().split())
nodes = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    L, R = map(int, read().split())
    nodes[R].append(L)


def bfs(num):
    q = deque([num])
    flag = [0] * (N+1)
    flag[num] = 1
    while q:
        next = q.popleft()
        visited[num] += 1
        for j in nodes[next]:
            if flag[j] == 0:
                flag[j] = 1
                q.append(j)


for i in range(1, len(nodes)):
    bfs(i)

max = max(visited)
for i in range(1, N+1):
    if max == visited[i]:
        print(i, end=' ')
