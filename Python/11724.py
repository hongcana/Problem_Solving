from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().split())

node = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, read().split())
    node[u].append(v)
    node[v].append(u)

visited = [0 for _ in range(N+1)]


def bfs(v):
    q = deque([])
    q.append(v)
    visited[v] = 1
    cnt = 1
    while q:
        start = q.popleft()
        if node[start]:
            for i in node[start]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
    return cnt


result = 0
for i in range(1, N+1):
    if not visited[i]:
        result += bfs(i)

print(result)
