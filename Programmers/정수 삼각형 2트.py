# DP
def solution(triangle):
    dp_tri = [ [ 0 for _ in range(i)] for i in range(1,len(triangle)+1)]
    dp_tri[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(0, i+1):
            # 왼끝
            if j == 0:
                dp_tri[i][j] = triangle[i][j] + dp_tri[i-1][j]
            
            # 오른끝
            elif j == i:
                dp_tri[i][j] = triangle[i][j] + dp_tri[i-1][j-1] 
            
            # 중앙
            else:
                dp_tri[i][j] = triangle[i][j] + max(dp_tri[i-1][j], dp_tri[i-1][j-1])
    return max(dp_tri[-1])