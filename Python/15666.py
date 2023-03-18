import sys
read = sys.stdin.readline
N, M = map(int, read().split())
num = sorted(set(list(map(int, read().split()))))
ans = []


def dfs():
    if len(ans) == M:
        print(*ans)
        return

    for i in num:
        if len(ans) >= 1:
            if ans[-1] <= i:
                ans.append(i)
                dfs()
                ans.pop()
        else:
            ans.append(i)
            dfs()
            ans.pop()


dfs()
