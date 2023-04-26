def solution(numbers, target):
    '''
    문제 풀이 유도는 DFS를 이용하라는 것 같았다.
    근데... 순수한 DFS 방법은 아니지만, 비슷하게 풀었다.
    n이 작아서 가능했던 방법.
    '''
    stack = [numbers[0], -numbers[0]]
    sum_list = []
    for i in range(1, len(numbers)):
        num = numbers[i]
        while stack:
            tmp = stack.pop()
            sum_list.append(tmp + num)
            sum_list.append(tmp - num)
        while sum_list:
            stack.append(sum_list.pop())
    answer = 0
    for s in stack:
        if s == target:
            answer += 1
    return answer
