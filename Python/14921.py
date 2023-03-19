import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = list(map(int, read().split()))
start = 0
end = N-1

# 용액이 음수면 start를 +1한다.
# 용액이 양수면 end를 -1한다.
# 그러면서 최소 결과값을 갱신한다.
# O(N)을 만족할 것이다.

result = li[start] + li[end]
while start < end:
    tmp = li[start] + li[end]
    if tmp == 0:
        result = 0
        break
    elif tmp > 0:
        end -= 1
    else:
        start += 1
    if abs(result) > abs(tmp):
        result = tmp

print(result)
