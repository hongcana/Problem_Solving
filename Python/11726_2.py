N = int(input())
dp = [ 0 for _ in range(N+1)] 
dp[1] = 1

for i in range(2, N+1):
    if i == 2:
        dp[i] = 2
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[N] % 10007)
