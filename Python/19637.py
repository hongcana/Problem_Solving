import sys
read = sys.stdin.readline
N, M = map(int, read().split())
li = []


def bsearch(t, start, end):
    if end < 0:
        return 0
    elif start > end:
        return start

    mid = (end + start) // 2
    if li[mid][1] == t:
        return mid
    else:
        if li[mid][1] > t:
            result = bsearch(t, start, mid-1)
        elif li[mid][1] < t:
            result = bsearch(t, mid+1, end)
    return result


plist = {}
for _ in range(N):
    name, point = map(str, read().split())
    if point in plist:
        continue
    else:
        plist[point] = name
        li.append([name, int(point)])

for t in range(M):
    t = int(read().rstrip())
    result = bsearch(t, 0, len(li)-1)
    print(li[result][0])
