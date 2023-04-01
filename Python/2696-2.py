import sys
import heapq
read = sys.stdin.readline

# heaq을 2개를 이용하며
# 중간값 보다 작은 값은 left, else: right heap
# left heap is max heap으로, why?
# 작은 힙에서 최댓값, 큰 힙에서 최솟값을 비교, 그리고 중앙 값을 비교해야 함.
# -1 // 4 // 5
# -3 -2 -1 // 4 // 5 => 여기서 -(-3), 4, 5를 비교해야함.
# -2 -1 // 4, -(-3) // 5
# 2번 삽입할 때 마다 중간값 교체 필요
# 만약 2개의 길이 같으면 = 그냥 중간값 유지

# 1
# 1 // 4
# 1 // 4 5


def checking(data):
    middle = data[0]
    left = []
    right = []
    result = [middle]
    for idx, val in enumerate(data[1:], 1):  # data[1:]부터, idx start =1
        if val >= middle:
            heapq.heappush(right, val)
        else:
            heapq.heappush(left, -val)

        if idx % 2 == 0:
            if len(left) < len(right):
                heapq.heappush(left, -middle)
                middle = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, middle)
                middle = -heapq.heappop(left)
            result.append(middle)

    print(len(result))

    for i in range(len(result)):
        if (i+1) != 1 and (i+1) % 10 == 1:
            print()
        print(result[i], end=" ")
    print()


N = int(read().rstrip())
for _ in range(N):
    M = int(read().rstrip())
    data = []

    if M % 10 == 0:
        for _ in range(M // 10):
            data.extend(list(map(int, read().split())))
    else:
        for _ in range(M // 10+1):
            data.extend(list(map(int, read().split())))

    checking(data)
