from collections import deque
import sys
read = sys.stdin.readline

N, K = map(int, read().split())
count = 0

visited = [0] * 100001

q = deque()
q.append(N)


def bfs(q):
    while q:
        now = q.popleft()
        if now == K:
            return visited[now]
        if 0 <= (now-1) < 100001 and visited[(now - 1)] == 0:
            visited[(now - 1)] = visited[now] + 1
            q.append(now-1)
        if 0 <= (now+1) < 100001 and visited[(now + 1)] == 0:
            visited[(now + 1)] = visited[now] + 1
            q.append(now+1)
        if 0 <= (now*2) < 100001 and visited[(now * 2)] == 0:
            visited[(now * 2)] = visited[now] + 1
            q.append(now*2)


print(bfs(q))
