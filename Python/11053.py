import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = list(map(int, read().split()))
dp = [1 for _ in range(len(li))]
for i in range(1, N):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
