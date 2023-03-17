import sys
read = sys.stdin.readline
T = int(read().rstrip())
for _ in range(T):
    n = int(read().rstrip())
    li = [list(map(int, read().split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)]
    if n == 1:
        print(max(li[0][0], li[1][0]))

    elif n == 2:
        print(max(li[0][0]+li[1][1], li[1][0]+li[0][1]))
    else:
        dp[0][0] = li[0][0]
        dp[1][0] = li[1][0]
        dp[0][1] = li[0][1] + li[1][0]
        dp[1][1] = li[1][1] + li[0][0]
        for i in range(2, n):
            dp[0][i] = li[0][i] + max(dp[0][i-2], dp[1][i-1], dp[1][i-2])
            dp[1][i] = li[1][i] + max(dp[1][i-2], dp[0][i-1], dp[0][i-2])
        print(max(dp[0][n-1], dp[1][n-1]))
