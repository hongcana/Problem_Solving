
def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return False

    if len(stack) > 0:
        return False
    else:
        return True