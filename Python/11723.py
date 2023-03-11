import sys
read = sys.stdin.readline

M = int(read())
s = []

for _ in range(M):
    comm = list(map(str, read().split()))
    if comm[0] == 'add':
        if int(comm[1]) in s:
            continue
        else:
            s.append(int(comm[1]))
    elif comm[0] == 'remove':
        if int(comm[1]) in s:
            s.remove(int(comm[1]))
    elif comm[0] == 'check':
        if int(comm[1]) in s:
            print(1)
        else:
            print(0)
    elif comm[0] == 'toggle':
        if int(comm[1]) in s:
            s.remove(int(comm[1]))
        else:
            s.append(int(comm[1]))
    elif comm[0] == 'all':
        s = []
        for i in range(1, 21):
            s.append(i)
    elif comm[0] == 'empty':
        s = []
