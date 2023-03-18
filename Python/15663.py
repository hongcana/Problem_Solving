import sys
read = sys.stdin.readline
N, M = map(int, read().split())
num = sorted(list(map(int, read().split())))
visited = [ 0 for _ in range(N)]

ans = []

def dfs():
    if len(ans) == M:
        print(*ans)
        return

    idx = -1
    for i in range(N):
        if visited[i] == 0 and idx != num[i]:
            visited[i] = 1
            ans.append(num[i])
            idx = num[i]
            dfs()
            visited[i] = 0
            ans.pop()

dfs()
