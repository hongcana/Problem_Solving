#DP로 풀죠..
#예..

import sys
read = sys.stdin.readline

N = int(input())
origin = [ list(map(int, input().split())) for _ in range(N)]
dp = [[ 1 for _ in range(3)] for _ in range(N)]

for i in range(N):
    # if 첫째줄
    if i == 0:
        for j in range(3):
            dp[i][j] = origin[i][j]

    # else 나머지줄
    else:
        for j in range(3):
            if j == 0:
                dp[i][j] = origin[i][j] + min(dp[i-1][1], dp[i-1][2])
            elif j == 1:
                dp[i][j] = origin[i][j] + min(dp[i-1][0], dp[i-1][2])
            else:
                dp[i][j] = origin[i][j] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))