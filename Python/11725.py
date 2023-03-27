import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

N = int(read().rstrip())
node = [[] for _ in range(N+1)]  # 0 안쓸거
visited = [0 for _ in range(N+1)]

for _ in range(N-1):
    S, E = map(int, read().split())
    node[S].append(E)
    node[E].append(S)


def dfs(v):
    for i in node[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)


dfs(1)

for i in range(2, N+1):
    print(visited[i])
