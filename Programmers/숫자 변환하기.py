from collections import deque


def solution(x, y, n):
    '''
    queue를 이용한 방식으로 풀이
    시간복잡도는 O(n)으로 판단. 명확히 따져보면 3n인데..
    이왜맞?
    dp를 이용한 풀이도 분명 존재할 것인데..
    '''
    if x == y:
        return 0
    q = deque()
    q.append([y, 0])

    while q:
        number, cnt = q.popleft()

        if number == x:
            return cnt
        if (number - n) > 0:
            q.append([number-n, cnt+1])
        if number % 2 == 0:
            q.append([number//2, cnt+1])
        if number % 3 == 0:
            q.append([number//3, cnt+1])
    return -1
