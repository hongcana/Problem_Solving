def solution(triangle):
    """
    전형적인 DP문제. 왜 Lv.3인가 이게?
    """
    answer = 0
    dp = []
    for t in triangle:
        dp.append([0]* len(t))
    for t in range(len(triangle)):
        for i in range(len(triangle[t])):
            if t == 0:
                dp[t][i] = triangle[t][i]
            if len(triangle) > (t+1): # 만약 다음 높이가 있다면
                    dp[t+1][i] = max(dp[t+1][i], dp[t][i]+triangle[t+1][i])
                    dp[t+1][i+1] =max(dp[t+1][i+1], dp[t][i]+triangle[t+1][i+1])
    return max(dp[-1])