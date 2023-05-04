
def solution(s, skip, index):
    """
    단순 문자열 문제
    이거를 뭐 ascii code를 이용해서 풀고 그럴 수도 있었겠지만은
    
    그냥 파이썬의 replace, find(), index를 적극 활용해서 풀이가능
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ans = ""

    for i in skip:
        alphabet = alphabet.replace(i,"")

    for i in s:
        ans += alphabet[(alphabet.find(i)+index) % len(alphabet)]
    
    return ans