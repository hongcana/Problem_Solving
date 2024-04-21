def solution(s):
    dic = {}
    answer = []
    
    order = 0
    for i in s:
        order += 1
        if i not in dic:
            dic[i] = order
            answer.append(-1)
        elif i in dic:
            answer.append(order - dic[i])
            dic[i] = order
    print(dic)
    return answer