import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
target = sum(m[:])
answer = 0
temp = m[0]

# 벌벌꿀
for i in range(1, n):
    temp += m[i]
    # ex) -4(m[0]), -8(temp), -4(m[1])
    # 이러면 첫 번째 벌이 m[i]도 먹을 수 없다는 것이 반영됨
    answer = max(answer, target - m[0] - m[i] + target - temp)

# 꿀벌벌
m.reverse()
temp = m[0]
for i in range(1, n):
    temp += m[i]
    answer = max(answer, target - m[0] - m[i] + target - temp)

# 벌꿀벌
for i in range(1, n):
    answer = max(answer, target - m[0] - m[-1] + m[i])

print(answer)
