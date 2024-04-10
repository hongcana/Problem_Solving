import heapq as hq
import sys
read = sys.stdin.readline

# 딕셔너리로 가지고 있다가
# solved가 뜨면 리스트에서 해당 원소 지우고
# heapify로 다시 heap으로 만들어야 겠는걸..

# 리스트를 쓰게되면.. solved 로직에서 리스트를 전부 순차탐색 해야됨. O(N)이 발생하는데
# 이미 for _ in range(M) 에서 O(N)을 한번 돌리므로, O(N^2)이 발생하여 시간 초과
# 그래서. hash를 씁니다. dict = O(1)

dic = {}
# 난이도 min heap
minh = []
# 난이도 max heap
maxh = []

N = int(read().rstrip())
for _ in range(N):
    P, L = map(int, read().split())
    dic[P] = L
    hq.heappush(minh, (L, P))
    hq.heappush(maxh, (-L, -P))
M = int(read().rstrip())

ans = []

for _ in range(M):
    command = list(read().split())

    if command[0] == "add":
        P, L = int(command[1]), int(command[2])
        hq.heappush(minh, (L, P))
        hq.heappush(maxh, (-L, -P))
        dic[P] = L

    elif command[0] == "solved":
        P = int(command[1])
        dic[P] = 0

    elif command[0] == "recommend":
        
        # 가장 어려운 문제 뽑기
        if command[1] == "1":
            while maxh and dic[-maxh[0][1]] != -(maxh[0][0]):
                hq.heappop(maxh)
            ans.append(-maxh[0][1])
            
        # 가장 쉬운 문제 뽑기
        elif command[1] == "-1":
            while minh and dic[minh[0][1]] != (minh[0][0]):
                hq.heappop(minh)
            ans.append(minh[0][1])

for a in ans:
    print(a)