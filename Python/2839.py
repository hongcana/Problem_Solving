
# 봉지 최소 개수
N = int(input())

dp = [ -1 for _ in range(N+1) ]

dp[0] = -1
dp[1] = -1
dp[2] = -1

for i in range(3, N+1):
    if i == 3 or i == 5:
        dp[i] = 1
    elif (dp[i-5] < 0) and (dp[i-3] < 0):
        dp[i] = -1
    elif (dp[i-5] < 0):
        dp[i] = dp[i-3] + 1
    elif (dp[i-3] < 0):
        dp[i] = dp[i-5] + 1
    else:
        dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)

# 정답 출력
print(dp[N])



# greedy version

result = 0

while N >= 0:
    if N % 5 == 0:
        result += (N // 5)
        print(result)
        break
    result += 1
    N -= 3
else:
    print(-1)
