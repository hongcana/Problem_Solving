def solution(survey, choices):
    # 성격을 담은 딕셔너리
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    li = ['R','T','C','F','J','M','A','N']
    
    answer = []
    
    for i in range(len(choices)):
        if choices[i] == 7:
            dic[survey[i][1]] += 3
        elif choices[i] == 6:
            dic[survey[i][1]] += 2
        elif choices[i] == 5:
            dic[survey[i][1]] += 1
        elif choices[i] == 3:
            dic[survey[i][0]] += 1
        elif choices[i] == 2:
            dic[survey[i][0]] += 2
        elif choices[i] == 1:
            dic[survey[i][0]] += 3

    for i in range(0,8,2):
        if dic[li[i]] >= dic[li[i+1]]:
            answer.append(li[i])
        else:
            answer.append(li[i+1])
    return ''.join(answer)