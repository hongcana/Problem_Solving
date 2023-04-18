import sys
read = sys.stdin.readline
N, M = map(int, read().split())
li = [int(read().rstrip()) for _ in range(N)]

def bs(start, end, target):
    total = 0
    while start <= end:
        mid = (start+end)//2
        result = 0
        for i in li:
            if mid >= i:
                result += mid // i
        if target > result:
            start = mid+1
        else:
            end = mid-1
            total = mid
    return total

print(bs(0, M*max(li), M))