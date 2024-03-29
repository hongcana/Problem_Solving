# BACKTRACKING
import sys
read = sys.stdin.readline
N, M = map(int, read().split())
ans = []
visited = [0 for _ in range(N+1)]


def dfs():
    if len(ans) == M:
        print(*ans)
        return

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            ans.append(i)
            dfs()
            visited[i] = 0
            ans.pop()


dfs()
