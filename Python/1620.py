import sys
read = sys.stdin.readline
N, M = map(int, read().split())
di = {}
li = []
ans = []
for i in range(1, N+1):
    k = read().rstrip()
    di[k] = i
    li.append(k)

for _ in range(M):
    comm = read().rstrip()
    if comm.isdigit() == True:
        ans.append(li[int(comm)-1])
    else:
        ans.append(di.get(comm))
for l in ans:
    print(l)
