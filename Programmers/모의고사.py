def solution(answers):
    answer = [0,0,0]
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(0,len(answers)):
        if answers[i] == a[i%len(a)]:
            answer[0] += 1
        if answers[i] == b[i%len(b)]:
            answer[1] += 1
        if answers[i] == c[i%len(c)]:
            answer[2] += 1
    
    re = []
    ans = max(answer)
    for i in range(0, len(answer)):
        if answer[i] == ans:
            re.append(i+1)
    return re