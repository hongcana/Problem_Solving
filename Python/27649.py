

S = input()

output = []
stack = []

sep1 = ['<', '>', '(', ')']
sep2 = ['&', '|']
double_cnt = 0

for i in S:
    # 공백인 경우
    if i == " ":
        # stack에 들어간 단어들을 조합후 output에 토큰화
        if len(stack) >= 1:
            output.append("".join(stack))
        stack = []

    # 구분자인 경우
    elif i in sep1:
        if len(stack) >= 1:
            output.append("".join(stack))
        output.append(i) # 구분자 추가
        stack = []

    # 짝수개 구분자인 경우
    elif i in sep2:
        if double_cnt == 1:
            double_cnt = 0
            stack = []
        else:
            if len(stack) >= 1:
                output.append("".join(stack))
            output.append(f'{i*2}')
            double_cnt = 1


    # 그냥 문자열인 경우
    else:
        stack.append(i)

# 나머지 마지막 문자들 추가
output.append("".join(stack))

if len(output) > 0:
    print(" ".join(output))