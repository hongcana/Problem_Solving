import sys
read = sys.stdin.readline

N, K = map(int, read().split())
moneys = []
for _ in range(N):
    moneys.append(int(read()))

moneys.sort(reverse=True)
count = 0
for m in moneys:
    if m > K:
        continue
    else:
        count += K // m
        K %= m
        if K <= 0:
            break
print(count)
