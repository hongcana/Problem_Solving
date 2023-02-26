import sys
read = sys.stdin.readline

N = int(read())
s = set()

for _ in range(N):
    s.add(read().rstrip())

li = list(s)
li.sort(key=lambda x: (len(x), x))

for i in li:
    print(i)