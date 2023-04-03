import sys
read = sys.stdin.readline
N, M, R = map(int, read().split())
sys.setrecursionlimit(10**9)

nodes = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, read().split())
    nodes[u].append(v)
    nodes[v].append(u)

for n in nodes:
    n.sort()

visited = [0 for _ in range(N+1)]

cnt = 1


def dfs(start):
    global cnt
    visited[start] = cnt
    cnt += 1
    for i in nodes[start]:
        if not visited[i]:
            dfs(i)


dfs(R)

for v in visited[1:]:
    print(v)
