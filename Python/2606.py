import sys
read = sys.stdin.readline

N = int(read())
M = int(read())

nodes = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, read().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = [0] * (N+1)


def dfs(nodes, start, visited):
    visited[start] = 1

    for i in nodes[start]:
        if not visited[i]:
            dfs(nodes, i, visited)

# global(전역변수) count 하나 만들어서
# 방문할때 마다 count += 1 하는 방법도 있음
# dfs parameter에 굳이 nodes, visited를 포함하지 않아도 될수도


dfs(nodes, 1, visited)
print(sum(visited)-1)
