import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = []
for _ in range(N):
    li.append(list(map(int, read().split())))


def search(start, sumval):
    global val
    if start + li[start][0] > N:
        return 0
    sumval += li[start][1]
    next = start + li[start][0]

    for j in range(next, N):
        if (start+li[j][0]) <= N:
            val = max(val, search(j, sumval))
    return max(val, sumval)


result = 0
for i in range(0, N):
    val = 0
    tmp = search(i, 0)
    if tmp > result:
        result = tmp
print(result)
