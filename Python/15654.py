import sys
read = sys.stdin.readline
N, M = map(int, read().split())
num = list(map(int, read().split()))
num.sort()
ans = []
visited = [0 for i in range(max(num)+1)]


def dfs(n, li):
    if n == M:
        ans.append(li)
        return

    for i in num:
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, li+[i])
            visited[i] = 0


dfs(0, [])
for a in ans:
    print(*a)
