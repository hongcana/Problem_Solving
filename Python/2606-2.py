
v = int(input())
e = int(input())

graph = [ [] for _ in range(v+1) ]
visited = [ False for _ in range(v+1)]

for i in range(e):
    start, end = map(int, input().split(" "))
    graph[start].append(end)
    graph[end].append(start)

# dfs 하죠
def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(sum(visited)-1)