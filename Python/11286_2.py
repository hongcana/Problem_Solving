import heapq as hq
import sys
read = sys.stdin.readline

N = int(read().rstrip())
absh = []
for _ in range(N):
    x = int(read().rstrip())
    if x != 0:
        hq.heappush(absh, (abs(x), x))
    else:
        if len(absh) == 0:
            print(0)
        else:
            print(hq.heappop(absh)[1])