import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, M, R = map(int, read().split())
nodes = [ [] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, read().split())
    nodes[u].append(v)
    nodes[v].append(u)

for n in nodes:
    n.sort(reverse=True)

cnt = 0


def dfs(start):
    global cnt
    cnt += 1
    visited[start] = cnt
    for i in nodes[start]:
        if not visited[i]:
            dfs(i)


dfs(R)

for v in visited[1:]:
    print(v)
