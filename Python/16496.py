from functools import cmp_to_key
import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = list(map(str, read().split()))


def comp(x, y):
    if x+y > y+x:
        return -1  # 순서 안바뀜
    else:
        return 1  # 순서 바뀜


li.sort(key=cmp_to_key(comp))
if int(''.join(li)) == 0:
    print(0)
else:
    print(''.join(li))