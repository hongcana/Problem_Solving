import sys
input = sys.stdin.readline
n, s = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0


def bt(idx, pre_sum):
    global cnt
    if idx >= n:
        return
    pre_sum += li[idx]

    if pre_sum == s:
        cnt += 1

    bt(idx+1, pre_sum)
    bt(idx+1, pre_sum-li[idx])


bt(0, 0)  # idx와 수열의 부분합
print(cnt)
