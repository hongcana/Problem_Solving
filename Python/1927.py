import heapq
import sys
read = sys.stdin.readline
N = int(read().rstrip())

hq = []
for _ in range(N):
    comm = int(read().rstrip())
    if comm == 0 and len(hq) != 0:
        print(hq[0])
        heapq.heappop(hq)
    elif comm == 0 and len(hq) == 0:
        print(0)
    else:
        heapq.heappush(hq, comm)
