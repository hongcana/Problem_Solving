def solution(n, lost, reserve):
    """
    n줬는데 왜 len(students)-1를 쓰셨나요? 피곤해서요..
    """
    students = [ 1 for _ in range(n+2)] # 1 1 1 1 1 1 1
    
    for r in reserve:
        students[r] += 1
    for l in lost:
        students[l] -= 1
        
    for i in range(1, len(students)-1):
        # 빌려줄 수 있어? 기준으로 체크            
        if students[i] == 2 and students[i-1] == 0:
            students[i] -= 1
            students[i-1] += 1
        
        elif students[i] == 2 and students[i+1] == 0:
            students[i] -= 1
            students[i+1] += 1
            
    ans = 0
    for i in range(1, len(students)-1):
        if students[i]:
            ans += 1
    return ans