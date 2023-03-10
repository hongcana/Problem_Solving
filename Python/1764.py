import sys
read = sys.stdin.readline
N, M = map(int, read().split())
hear = set()
see = set()
for i in range(N):
    hear.add(read().rstrip())
for i in range(M):
    see.add(read().rstrip())
print(len(hear & see))
for i in sorted(list(hear & see)):
    print(i)
