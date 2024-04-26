def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)+1):
        total = []
        for j in range(0, len(s), i):
            key = s[j:j+i]
            total.append(key)
        #print(total)
        cmp_t = ''
        if len(total) == 1:
            cmp_t += str(total)
        else:
            point = 1
            for k in range(0, len(total)-1):
                if total[k] == total[k+1]:
                    point += 1
                else:
                    if point == 1:
                        cmp_t += total[k]
                    else:
                        cmp_t = cmp_t + str(point) + total[k] 
                        point = 1
            # 마지막
            if point == 1:
                cmp_t += total[-1]
            else:
                cmp_t = cmp_t + str(point) + total[k]
                        
        #print(cmp_t, len(cmp_t))
        answer = min(answer, len(cmp_t))
    return answer