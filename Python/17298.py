import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = list(map(int, read().split()))

stack = []
result = [-1 for _ in range(N)]

for i in range(N):
    while stack and li[stack[-1]] < li[i]:
        result[stack.pop()] = li[i]
    stack.append(i)

print(*result)
