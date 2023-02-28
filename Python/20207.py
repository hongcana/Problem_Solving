import sys
read = sys.stdin.readline

N = int(read())
date = []

for _ in range(N):
    date.append(list(map(int, read().split())))

date.sort(key=lambda x: x[0])
cal = [0 for _ in range(max(date, key=lambda x: x[1])[1])]

for d in date:
    for j in range(d[0]-1, d[1]):
        cal[j] += 1

start = 0
result = 0
on = 0

for i in range(len(cal)):
    if cal[i] != 0 and on == 0:
        start = i
        on = 1

    elif cal[i] == 0 and on != 0:
        result += (i-start) * max(cal[start:i])
        start = 0
        on = 0

if on != 0:
    result += (len(cal)-start) * max(cal[start:len(cal)])

print(result)
