import heapq
import sys
read = sys.stdin.readline
N = int(read().rstrip())
hq = []

for _ in range(N):
    comm = int(read().rstrip())
    if comm == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(-hq[0])
            heapq.heappop(hq)
    else:
        heapq.heappush(hq, -comm)