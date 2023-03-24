import sys
read = sys.stdin.readline
N = int(read().rstrip())
visited = [False] * N
q = [(N, 0)]
parent = [0] * N
idx = 0

while idx < len(q):
    val, dist = q[idx]
    idx += 1
    if val == 1:
        print(dist)
        break
    for i in range(2, 4):
        if not visited[val//i] and val % i == 0:
            visited[val//i] = True
            q.append((val//i, dist+1))
            parent[val//i] = val
    if not visited[val-1]:
        visited[val-1] = True
        q.append((val - 1, dist+1))
        parent[val-1] = val

value = 1
path = ['1']
while value != N:
    value = parent[value]
    path.append(str(value))

print(" ".join(reversed(path)))