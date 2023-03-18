import sys
read = sys.stdin.readline


def isTidy(n):
    return list(str(n)) == sorted(list(str(n)))


T = int(read().rstrip())
for tc in range(1, T+1):
    num = int(read().rstrip())
    if isTidy(num):
        print(f"Case #{tc}: {int(num)}")
    else:
        length = len(str(num))
        for i in range(1, length):
            a, b = divmod(num, 10**i)
            tp = str(a-1)+'9'*len(str(b))
            if isTidy(tp):
                print(f"Case #{tc}: {int(tp)}")
                break
