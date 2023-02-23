import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
crn = list(map(int, read().split()))
M = int(read())
box = list(map(int, read().split()))


crn.sort(reverse=True)
box.sort(reverse=True)
box = deque(box)

ans = [0 for _ in range(N)]

if crn[0] < box[0]:
    ans = [-1]

else:
    while len(box):
        ans[0] += 1
        box.popleft()
        ret = 0

        for i in range(1, N):
            while ans[i] < ans[i-1]:
                if len(box) == 0:
                    ret = 1
                    break

                if crn[i] < box[0]:
                    ret = 1
                    break

                ans[i] += 1
                box.popleft()

            if ret:
                break

print(max(ans))
