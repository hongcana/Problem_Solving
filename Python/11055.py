import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = list(map(int, read().split()))
dp = li[:]
for i in range(N):
    for j in range(i):
        if li[i] > li[j] and dp[i] < dp[j] + li[i]:
            dp[i] = dp[j] + li[i]
    print(dp)
print(max(dp))
