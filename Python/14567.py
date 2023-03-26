import sys
read = sys.stdin.readline
N, M = map(int, read().split())
li = [1 for _ in range(N+1)]
comm = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, read().split())
    comm[i].append(j)

for i in range(1, N+1):
    for j in comm[i]:
        li[j] = max(li[j], li[i]+1)

print(*li[1:])
