import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = list(map(int, read().split()))
dp = [1 for _ in range(len(li))]
result = []
for i in range(1, N):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
re = max(dp)
for i in range(N-1, -1, -1):
    if dp[i] == re:
        result.append(li[i])
        re -= 1
for i in sorted(result):
    print(i, end=' ')
