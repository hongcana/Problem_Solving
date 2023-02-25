import sys
read = sys.stdin.readline

N = int(read())
li = list(map(int, read().split()))
li.sort()

for i in range(1, len(li)):
    li[i] += li[i-1]

print(sum(li))
