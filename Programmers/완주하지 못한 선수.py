def solution(participant, completion):
    """
    이렇게 안하고, from collections import Counter를 이용한 풀이도 존재.
    from collections import Counter

    def solution(participant, completion):
        dict = Counter(participant) - Counter(completion)
        return list(dict)[0]
    """
    dic = {}
    
    for p in participant:
        dic[p] = dic.get(p, 0) + 1 # get = O(1)
    for c in completion:
        dic[c] -= 1 #dic 접근 = 해시 함수를 이용하여 O(1)
    
    answer = ''
    for k,v in dic.items(): # O(N)
        if v >= 1:
            answer = k
    return answer