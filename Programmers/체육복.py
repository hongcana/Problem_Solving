def solution(n, lost, reserve):
    """
    전형적인 그리디 알고리즘으로 해결할 수 있는 문제,
    체육복을 빌려줄 수 있는 학생이 앞,뒤로 lost를 체크할 수 있게 만드는게 핵심
    O(n)이 지배적인데, n이 30이하라서 충분히 해결 가능.
    """
    students = [1 for _ in range(n+2)]
    for i in lost:
        students[i] -= 1
    for i in reserve:
        students[i] += 1

    for i in range(1, n+1):  # ex) 1 [1,1,1,1,1] 1
        if students[i] == 2:
            if students[i-1] == 0:
                students[i] -= 1
                students[i-1] += 1
            elif students[i+1] == 0:
                students[i] -= 1
                students[i+1] += 1

    answer = 0
    for i in range(1, n+1):
        answer += 1 if students[i] else 0
    return answer
