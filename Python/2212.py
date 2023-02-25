import sys
read = sys.stdin.readline

N = int(read())
K = int(read())
sensors = list(map(int, read().split()))

sensors.sort(reverse=True)
ans = []

for i in range(0, len(sensors)-1):
    ans.append(sensors[i] - sensors[i+1])

ans.sort()

print(sum(ans[:N-K]))

# 1 3 6 6 7 9
# 3 2 0 1 2
# 3 2 2 1 0
# 합계 32, 절반 16

# 2개 일때 5
# 3개 일때 3
# [6~9] [1~1] [3~3] = 3인데?
# 4개 일때
# [1~1] [3~3] [6~7] [9~9] = 1영역
