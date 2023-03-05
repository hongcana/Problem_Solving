# DFS, 다시풀기, 특히 트리의 지름에 대해 생각해보기..
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(read())
nodes = []

for _ in range(N+1):
    nodes.append([])

for _ in range(0, N-1):
    i, j, k = map(int, read().split())
    nodes[i].append([j, k])
    nodes[j].append([i, k])


def dfs(x, w):
    for i in nodes[x]:
        a, b = i  # ex) 2, 3
        if d[a] == -1:  # 아직 방문하지 않았으면
            d[a] = w+b  # 해당 노드 -> 기존 가중치 + 새로운 가중치
            dfs(a, w+b)  # 해당 노드에서 dfs


# 루트 노드에서 가장 먼 곳을 찾기.
d = [-1] * (N+1)
d[1] = 0
dfs(1, 0)  # 루트 노드부터, 가중치 0임

# 위에서 찾은 노드에서 가장 먼 노드 찾기
start = d.index(max(d))
d = [-1] * (N+1)
d[start] = 0
dfs(start, 0)

print(max(d))
