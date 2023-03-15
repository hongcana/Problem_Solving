from collections import deque
import sys
read = sys.stdin.readline
A, B = map(int, read().split())
cnt = 0
q = deque([B])
while q:
    cnt += 1
    if q[0] == A:
        break
    start = q.popleft()
    if start >= 10 and str(start)[-1] == '1':
        q.append(int(str(start)[0:-1]))
    elif start % 2 == 0:
        q.append(start // 2)

if len(q) == 0:
    print(-1)
else:
    print(cnt)
