import sys
N, K = map(int, sys.stdin.readline().split(" "))
li = list(map(int, sys.stdin.readline().split(" ")))

dic = {}
ans = 0
bf_ans = 0
i = 0
start = 0

while i < N:
    if li[i] not in dic:
        dic[li[i]] = 1
        ans += 1
        i += 1
    else:
        if dic[li[i]]+1 <= K:
            dic[li[i]] += 1
            ans += 1
            i += 1
        else:
            dic = {}
            for j in range(start, i):
                if li[j] == li[i]:
                    start = j+1
                    i = j+1
                    break
            # dic[li[i]] = 1
            bf_ans = max(bf_ans, ans)
            ans = 0
print(max(bf_ans, ans))