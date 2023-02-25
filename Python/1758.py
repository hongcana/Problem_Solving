import sys
read = sys.stdin.readline

N = int(read())
customers = [int(read()) for _ in range(N)]
customers.sort(reverse=True)
sum = 0

for i, j in zip(customers, range(1, len(customers)+1)):
    if i - (j-1) < 0:
        break
    else:
        sum += i-(j-1)
print(sum)
