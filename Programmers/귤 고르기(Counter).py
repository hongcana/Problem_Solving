from collections import Counter
def solution(k, tangerine):
    """
    Collections의 Counter class를 이용한 풀이
    """
    new = Counter(tangerine)

    answer = 0
    for i in sorted(new.values(), reverse=True):
        if k > 0:
            answer += 1
            k -= i
    return answer