import sys
read = sys.stdin.readline

N = int(read())
li = [int(read()) for _ in range(N)]
li.sort(reverse=True)

sum = 0
for i in range(1, len(li)+1):
    if i % 3 == 0:
        pass
    else:
        sum += li[i-1]

print(sum)
