from collections import deque

def solution(cacheSize, c):
    """
    2017 카카오 난이도 하 문제
    LRU를 이용하고, 캐시히트, 캐시미스를 구현하는 문제
    queue를 이용하여 LRU를 구현해봄.
    """
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return len(c) * 5
    
    for i in range(len(c)):
        # 캐시미스
        if c[i].upper() not in cache:
            cache.append(c[i].upper())
            answer += 5
            
            # 캐시에 공간이 부족하다면 LRU에 의거 교체
            if len(cache) > cacheSize:
                cache.popleft()

        # 캐시히트 -> LRU 순서를 맞춰주기
        else:
            answer += 1
            cache.remove(c[i].upper())
            cache.append(c[i].upper())
    return answer
