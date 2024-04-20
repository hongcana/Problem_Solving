import sys
N, M = map(int, sys.stdin.readline().split(" "))
num = list(map(int, sys.stdin.readline().split(" ")))

# 1부터 n까지 합을 기록해놓은 table
dp = [ 0 for _ in range(N)]
dp[0] = num[0]
for i in range(1, N):
    dp[i] = num[i]+dp[i-1]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split(" "))

    if i == 1:
        print(dp[j-1])
    else:
        print(dp[j-1]-dp[i-2])