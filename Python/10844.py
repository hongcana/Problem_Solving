import sys
read = sys.stdin.readline
dp = []
N = int(read().rstrip())
for i in range(N+1):
    dp.append([0 for _ in range(10)])

# dp[1]
for i in range(1, 10):
    dp[1][i] = 1

if N >= 2:
    dp[2][0] = 1
    for j in range(1, 9):
        dp[2][j] = 2
    dp[2][9] = 1

for i in range(3, N+1):
    dp[i][0] = dp[i-1][1]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][9] = dp[i-1][8]

sum = 0
for i in range(1, 10):
    sum += dp[N][i]
print(sum % 1000000000)
