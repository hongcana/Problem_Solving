import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = list(map(int, read().split()))
M = int(read().rstrip())
tc = list(map(int, read().split()))
li.sort()


def bsearch(t, start, end):
    # 재귀의 종료 조건? mid == t
    mid = (end + start) // 2
    if start > end:
        return 0
    elif li[mid] == t:
        return 1
    else:
        # 만약 중간 지점이 t보다 크면
        if li[mid] > t:
            result = bsearch(t, start, mid-1)

        # 만약 중간 지점 값이 t보다 작으면
        elif li[mid] < t:
            result = bsearch(t, mid+1, end)
    return result


for t in tc:
    print(bsearch(t, 0, N-1), end=" ")
