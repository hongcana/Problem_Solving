from collections import deque


def solution(people, limit):
    people = deque(sorted(people))
    answer = 0
    while people:
        tempsum = 0  # 임시 합, limit 제한 확인용 변수
        tempsum += people.pop()  # 가장 큰 값인 맨 뒤에서 하나 뺀다.
        answer += 1
        if not people:  # 만약 큐에 원소가 없다면
            break
        while tempsum + people[0] <= limit:
            tempsum += people.popleft()  # limit가 찰때까지 작은 놈을 계속 태운다.
            if not people:
                break
    return answer
