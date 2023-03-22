import sys
read = sys.stdin.readline
N = int(read().rstrip())
dp = [0] * (N+1)
li = [list(map(int, read().split())) for _ in range(N)]

for i in range(N-1, -1, -1):
    if li[i][0] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], li[i][1] + dp[i + li[i][0]])
print(dp[0])