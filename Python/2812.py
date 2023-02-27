import sys
read = sys.stdin.readline

n, k = map(int, read().split())
numbers = read().rstrip()

arr = []
for number in numbers:
    while arr and 0 < k:
        if arr[-1] < number:
            arr.pop()
            k -= 1
        else:
            break
    arr.append(number)

if k != 0:
    for num in range(k):
        arr.pop()

print("".join(arr))

# ex
# 10 4
# 8 1 8 7 2 5 2 8 4 1
# 8
# 8 1
# 8 1(pop) 8
# 8 8 7
# 8 8 7 2
# 8 8 7 2(pop) 5
# 8 8 7 5 2
# 8 8 7 5(p) 2(p) 8
# 8 8 7 8 4 1
