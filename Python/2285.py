import sys
read = sys.stdin.readline

N = int(read())
li = [list(map(int, read().split())) for _ in range(N)]
li.sort(key=lambda x: x[0])

sum = 0
for i in li:
    sum += i[1]

sum = round(sum/2)

cmp = 0
for i in range(0, len(li)):
    cmp += li[i][1]
    if cmp >= sum:
        print(li[i][0])
        break
