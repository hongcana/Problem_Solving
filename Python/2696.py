import sys
from collections import deque
read = sys.stdin.readline
N = int(read().rstrip())

for _ in range(N):
    M = int(read().rstrip())
    result = []
    li = []
    while M != 0:
        query = deque(list(map(int, read().split())))
        for i in range(1, min(M+1, 11)):
            li.append(query.popleft())
            if i % 2 == 1:
                li.sort()
                result.append(li[len(li)//2])
        M = max(M-10, 0)

    print(len(result))
    if len(result) > 10:
        for i in range(0, (len(result)//10)+1):
            print(*result[10*i: min((10*i)+10, len(result))])
    else:
        print(*result)