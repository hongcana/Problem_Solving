import sys
read = sys.stdin.readline

T = int(read())
tc_result = [0 for _ in range(T)]

for i in range(T):
    N = int(read())
    prices = list(map(int, read().split()))

    prices.reverse()
    price_high = prices[0]
    result = 0
    for j in range(len(prices)):
        if price_high > prices[j]:
            result += price_high - prices[j]
        else:
            price_high = prices[j]
    tc_result[i] = result

for k in tc_result:
    print(k)
