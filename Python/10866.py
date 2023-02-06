from collections import deque
import sys

deq = deque()
num = int(input())

for _ in range(0, num):
    comm = sys.stdin.readline().split()

    if comm[0] == 'push_back':
        deq.append(int(comm[1]))
    elif comm[0] == 'push_front':
        deq.appendleft(int(comm[1]))
    elif comm[0] == 'front':
        print(deq[0]) if len(deq) != 0 else print(-1)
    elif comm[0] == 'back':
        print(deq[-1]) if len(deq) != 0 else print(-1)
    elif comm[0] == 'pop_front':
        if len(deq) != 0:
            print(deq[0])
            deq.popleft()
        else:
            print(-1)
    elif comm[0] == 'pop_back':
        if len(deq) != 0:
            print(deq[-1])
            deq.pop()
        else:
            print(-1)
    elif comm[0] == 'empty':
        print(1) if len(deq) == 0 else print(0)
    elif comm[0] == 'size':
        print(len(deq))