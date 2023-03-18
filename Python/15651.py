import sys
read = sys.stdin.readline
N, M = map(int, read().split())
ans = []


def dfs(n, li):
    if n == M:
        ans.append(li)
        return

    for i in range(1, N+1):
        dfs(n+1, li+[i])


dfs(0, [])
for i in ans:
    print(*i)
