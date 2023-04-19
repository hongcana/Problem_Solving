import sys
read = sys.stdin.readline
N = int(read().rstrip())

dp = [0 for _ in range(N+1)]
square = [i * i for i in range(1, N+1)]  # 1,4,9,16..

for i in range(1, N+1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i-j])
    dp[i] = min(s) + 1
print(dp[N])
