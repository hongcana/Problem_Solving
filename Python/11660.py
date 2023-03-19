import sys
read = sys.stdin.readline
N, M = map(int, read().split())
li = []
for _ in range(N):
    li.append(list(map(int, read().split())))

prefix = []
for r in range(N):
    sum_val = 0
    col = [0]  # 다음 p[right] - p[left-1] 계산에서 필요.
    for c in range(N):
        sum_val += li[r][c]
        col.append(sum_val)
    prefix.append(col)

for _ in range(M):
    x1, y1, x2, y2 = map(int, read().split())
    result = 0
    for i in range(x1-1, x2):
        result += prefix[i][y2] - prefix[i][y1-1]
    print(result)
