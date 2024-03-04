# lv.2 Greeeeeedy

def solution(number, k):
    i = 0
    while i < len(number) - 1 and k > 0:
        if number[i] < number[i+1]:
            number = number[:i] + number[i+1:] # 해당 숫자를 제외하는 로직
            k -= 1
            if i > 0:
                i = i - 2 # 이전 숫자 체크 가능하게
            else:
                i -= 1
        i += 1

    if k > 0:
        number = number[:len(number)-k]

    return number