import sys
read = sys.stdin.readline

seed = int(read())
stock_prices = list(map(int, read().split()))

joon_m = seed
joon_s = 0
seong_m = seed
seong_s = 0

streak = 0
for s in range(len(stock_prices)):
    joon_s += joon_m // stock_prices[s]
    joon_m = joon_m % stock_prices[s]

    if s == 0:
        pass
    else:
        if stock_prices[s-1] < stock_prices[s]:
            if streak > 0:
                streak += 1
            elif streak <= 0:
                streak = 1

        elif stock_prices[s-1] > stock_prices[s]:
            if streak < 0:
                streak -= 1
            elif streak >= 0:
                streak = -1

        elif stock_prices[s-1] == stock_prices[s]:
            streak = 0

        if streak >= 3 and seong_s != 0:
            seong_m += seong_s * stock_prices[s]
            seong_s = 0

        if streak <= -3:
            seong_s += seong_m // stock_prices[s]
            seong_m = seong_m % stock_prices[s]

if ((joon_m + joon_s * stock_prices[-1]) > (seong_m + seong_s * stock_prices[-1])):
    print("BNP")
elif ((joon_m + joon_s * stock_prices[-1]) < (seong_m + seong_s * stock_prices[-1])):
    print("TIMING")
else:
    print("SAMESAME")
