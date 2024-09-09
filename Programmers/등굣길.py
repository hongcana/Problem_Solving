def solution(m, n, puddles):
    # 이 문제는 (y,x) 열행으로 주어짐
    dp = [[1 for _ in range(m)] for _ in range(n)]
    
    for i in puddles:
        # 행에서 웅덩이가 나오는데 첫 줄이면,
        if i[1] == 1: # ex)  [2,1]
            for j in range(i[0]-1, len(dp[0])):
                dp[0][j] = 0 # 그 열부터 끝 열까지 첫줄은 모두 경우의수 0으로
        # 첫 열 쫙 밀기
        elif i[0] == 1: # 1 2
            for j in range(i[1]-1, len(dp)):
                dp[j][0] = 0
        else:
            dp[i[1]-1][i[0]-1] = 0
    
    # 첫째
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            # 물웅덩이가 아니면
            if dp[i][j] > 0:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    print(dp)
    return (dp[n-1][m-1]) % 1000000007