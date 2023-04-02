import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = list(map(int, read().split()))
wholesum = sum(li)

if wholesum % 3 != 0:
    print("NO")

else:
    tu = wholesum // 3
    result = 0
    cnt = 0
    for i in range(N):
        result += li[i] // 2
    if tu <= result:
        cnt = 1
    print("YES" if cnt else "NO")
