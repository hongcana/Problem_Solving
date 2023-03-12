import sys
read = sys.stdin.readline
write = sys.stdout.write
li = [0]
M = int(read().rstrip())
sum = 0
xor = 0
for i in range(1, M+1):
    comm = list(map(int, read().split()))
    if comm[0] == 1:
        li.append(comm[1])
        sum += comm[1]
        xor ^= comm[1]
    elif comm[0] == 2:
        sum -= comm[1]
        xor ^= comm[1]
    elif comm[0] == 3:
        write(str(sum) + "\n")
    elif comm[0] == 4:
        write(str(xor) + "\n")
