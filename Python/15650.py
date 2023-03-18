# BACKTRACKING
import sys
read = sys.stdin.readline
N, M = map(int, read().split())
ans = []
visited = [0 for _ in range(N+1)]


def dfs(n, li):
    if n == M:
        ans.append(li)
        return

    for i in range(1, N+1):
        if len(li) == 0:
            visited[i] = 1
            dfs(n+1, li+[i])
            visited[i] = 0
        else:
            if visited[i] == 0 and li[-1] < i:
                visited[i] = 1
                dfs(n+1, li+[i])
                visited[i] = 0


dfs(0, [])
for li in ans:
    print(*li)
