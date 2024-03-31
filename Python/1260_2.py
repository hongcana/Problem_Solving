
from collections import deque

def dfs(graph, start, visited_dfs):
    visited_dfs[start] = True
    print(start, end = " ")
    for i in graph[start]:
        if visited_dfs[i] == 0:
            dfs(graph, i, visited_dfs)

def bfs(graph, start, visited_bfs):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited_bfs[i] == 0:
                queue.append(i)
                visited_bfs[i] = True


N, M, V = map(int, input().split(" "))

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

dfs(graph, V, visited_dfs)
print("")
bfs(graph, V, visited_bfs)