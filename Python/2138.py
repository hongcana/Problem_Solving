import sys
import heapq
heap = []
read = sys.stdin.readline
n = int(read().rstrip())
li = []
for i in range(n):
    a, b = map(int, input().split())
    li.append([a, b])
li.sort(key=lambda x: x[0])
heapq.heappush(heap, li[0][1])

for i in range(1, n):
    if heap[0] > li[i][0]:
        heapq.heappush(heap, li[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, li[i][1])
print(len(heap))