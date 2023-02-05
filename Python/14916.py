num = int(input())
count = 0

while True:
    if (num >= 5) and (num % 5) % 2 != 0:
        count += 1
        num -= 2
    elif (num >= 5) and (num % 5) % 2 == 0:
        count += 1
        num -= 5
    if num == 0:
        break
    elif (num < 5) and (num % 2 == 0):
        count += num // 2
        num %= 2
    elif (num < 5) and (num % 2 != 0):
        count = -1
        break

print(count)
