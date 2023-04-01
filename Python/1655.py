import sys
import heapq
read = sys.stdin.readline
N = int(read().rstrip())

data = []
for _ in range(N):
    data.append(int(read().rstrip()))

middle = data[0]
result = [middle]
left, right = [], []

for idx, val in enumerate(data[1:], 2):
    if val >= middle:
        heapq.heappush(right, val)
    else:
        heapq.heappush(left, -val)

    if len(right) > len(left)+1:
        heapq.heappush(left, -middle)
        middle = heapq.heappop(right)
    elif len(right) < len(left):
        heapq.heappush(right, middle)
        middle = -heapq.heappop(left)
    result.append(middle)

for r in result:
    print(r)
