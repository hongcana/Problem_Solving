import sys
import bisect
read = sys.stdin.readline
N, M = map(int, read().split())
li = []
pwr = []
for _ in range(N):
    name, point = map(str, read().split())
    li.append(name)
    pwr.append(int(point))

for t in range(M):
    t = int(read().rstrip())
    result = bisect.bisect_left(pwr, t)
    print(li[result])
