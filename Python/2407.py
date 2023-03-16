import sys
read = sys.stdin.readline
N, M = map(int, read().split())

# 0 안씀
dp = [0 for _ in range(N+1)]
dp[1] = 1
for i in range(2, N+1):
    dp[i] = i * dp[i-1]
if N == M:
    print(dp[N])
    # N! / N-r
if N != M:
    print(dp[N] // (dp[(N-M)] * dp[M]))