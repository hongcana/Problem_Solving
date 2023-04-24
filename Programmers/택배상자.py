from collections import deque

def solution(order):
    '''
    지배 받는 시간복잡도 : O(N) -> order 탐색
    완전탐색? 아니면 그냥 스택문제 느낌?
    '''
    answer = 0
    N = len(order)
    order = deque(order)
    stack = [] # 보조 컨테이너 벨트
    i = 1 # 상자 번호

    while order:
        # 현재 컨테이너 벨트의 상자 번호가 트럭에 실어야 하는 순서와 일치하다면,
        if order[0] == i:
            answer += 1
            order.popleft()
            i += 1
            if not order:
                break
            
        # 보조 컨테이너에서 실을 수 있다면
        elif len(stack) > 0 and stack[-1] == order[0]:
            stack.pop()
            order.popleft()
            answer += 1
            if not order:
                break
        
        # 그렇지 않다면, 만약 현재 보조 컨테이너에 실을 수 있는 상자 번호가 order 번호보다 크다면?
        # ex) i = 5인데 3번째 상자를 실어야하고, 보조 컨테이너[0]는 2라면?
        elif i > order[0] and stack[-1] != order[0]:
            break
            
        else:
            stack.append(i)
            i+=1
    return answer