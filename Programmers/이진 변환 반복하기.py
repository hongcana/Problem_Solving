def solution(s):
    """
    이진 변환하는 함수인 bin()을 아느냐가 핵심
    bin()의 결과값은 '0b010101...'이렇게 나오므로, '0b' 부분을 잘라줘야
    """
    remove_count = 0
    iterations = 0

    while s != "1":
        iterations += 1

        new = ""
        for i in s:
            if i == '1':
                new += i 
            else:
                remove_count += 1
        new = str(bin(len(new)))[2:]
        s = new

    return [iterations, remove_count]

print(solution("110010101001"))