# dp[4] = 4번째 잔 => 2,3이냐 1,2, 4냐 1, 3,4냐 등등..
# max(dp[i-2]+li[i], dp[i-3]+li[i-1]+li[i], dp[i-1])

import sys
read = sys.stdin.readline
n = int(read().rstrip())
li = [0]
for _ in range(n):
    li.append(int(read().rstrip()))
dp = [0 for _ in range(n+1)]

if n == 1:
    print(li[1])

else:
    dp[1] = li[1]
    dp[2] = li[2]+li[1]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2]+li[i], dp[i-3]+li[i-1]+li[i], dp[i-1])

    print(max(dp))
