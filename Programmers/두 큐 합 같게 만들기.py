from collections import deque

# 원소의 합이 큰 쪽에서 작은 쪽으로 옮기는데?

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = (len(queue1) + len(queue2)) * 2 # 원래대로 돌아오는게 최대 경우의 수?
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2
    
    while True:
        if sum1 > sum2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            answer += 1
        elif sum1 < sum2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
            answer += 1
        else:
            break
        if answer == limit: # 한계치에 도달하면 -1 리턴
            return -1
    return answer