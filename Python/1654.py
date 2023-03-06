import sys
read = sys.stdin.readline

K, N = map(int, read().split())
lines = []
for _ in range(K):
    lines.append(int(read().rstrip()))

start = 1
end = max(lines)

result = 0
while (start <= end):
    mid = (start + end) // 2
    total = 0
    for i in lines:
        # 자를 수 있으면
        if i >= mid:
            total += i // mid  # 몫을 더해줌
    # 더 작게 잘라야 하는가?
    if total < N:
        end = mid - 1
    # 더 작게 자를 필요가 없는가?
    else:
        start = mid+1
        result = mid
print(result)
