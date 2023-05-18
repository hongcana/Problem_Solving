def solution(k, tangerine):
    """
    딕셔너리를 이용한 그리디 풀이법
    시간복잡도 = sorted()에서 O(N log N)소요
    딕셔너리의 get함수, sorted()함수와 items()+lambda 활용
    """
    dic = {}
    
    for t in tangerine:
        dic[t] = dic.get(t, 0) + 1

    dic = dict(sorted(dic.items(), key=lambda x : (x[1], -x[0]), reverse=True)) # value값 기준 내림차순 + key값 기준 오름차순
    answer = []
    
    for d in dic:
        # 만약 k보다 dic[d] 값이 작다면
        if dic[d] <= k:
            k -= dic[d] # 개수만큼 귤의 개수인 k를 차감
            answer.append(d) # 해당 무게 포함
        else: # 남은 k 값이 있다면 해당 무게 포함후 종료
            if k > 0:
                answer.append(d)
            break
    return len(answer)

print(solution(6, [1,3,2,5,4,5,2,3]))