import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = [0] * N
ans = 0


def checking(num):
    for i in range(num):
        if li[num] == li[i] or (abs(li[num] - li[i]) == num - i):
            return False
    return True


def dfs(row):
    global ans
    if row == N:
        ans += 1
        return

    for c in range(N):
        li[row] = c
        if checking(row):
            dfs(row+1)


dfs(0)
print(ans)
