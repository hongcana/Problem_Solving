# max heap, min heap 2개 가동하자
# recommend 1 = max heap
# recommend -1 = min heap

import heapq
import sys
read = sys.stdin.readline
N = int(read().rstrip())

maxh = []
minh = []
q = {}

for _ in range(N):
    v, k = map(int, read().split())
    heapq.heappush(minh, (k, v))
    heapq.heappush(maxh, (-k, -v))
    q[v] = k
M = int(read().rstrip())

for _ in range(M):
    comm = list(map(str, read().split()))

    if comm[0] == 'recommend':
        if int(comm[1]) == 1:
            while maxh and q[-maxh[0][1]] != -(maxh[0][0]):
                heapq.heappop(maxh)
            print(-maxh[0][1])
        else:
            while minh and q[minh[0][1]] != (minh[0][0]): # q번호와 다르면 알아서 pop
                heapq.heappop(minh) # 이후 트리의 루트 노드 q는 딕셔너리 value 참조후 비교
            print(minh[0][1])
    elif comm[0] == "add":
        v, k = int(comm[1]), int(comm[2])
        heapq.heappush(minh, (k, v))
        heapq.heappush(maxh, (-k, -v))
        if not q.get(v):
            q[v] = 0
        q[v] = k
    elif comm[0] == "solved":
        target = int(comm[1])
        q[target] = 0
