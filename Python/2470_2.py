# 두 용액 2번째 풀이
# using two-pointer
import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = list(map(int, read().split()))
li.sort()
start = 0
end = N-1

result = li[start] + li[end]
pos = [li[start], li[end]]
while start < end:
    tmp = li[start] + li[end]
    if abs(result) > abs(tmp):
        result = tmp
        pos = [li[start], li[end]]
    if tmp == 0:
        pos = [li[start], li[end]]
        break
    elif tmp > 0:
        end -= 1
    else:
        start += 1

print(*pos)
