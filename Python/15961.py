# 문제를 잘 읽자..

import sys
N, d, k, c = map(int, sys.stdin.readline().split(" "))

sushi = []
for i in range(0, N+k):
    if i >= N:
        sushi.append(sushi[i-N])
    else:
        num = int(sys.stdin.readline())
        sushi.append(num)

su = {}
longest = 0

for i in range(0, k):
    if sushi[i] not in su:
        su[sushi[i]] = 1
    else:
        su[sushi[i]] += 1
    longest = len(su)
    if c not in su:
        longest += 1
#print(su, longest)
    
for s in range(1, N):
    # 앞 뺌
    if su[sushi[s-1]] > 1:
        su[sushi[s-1]] -= 1
    else:
        su.pop(sushi[s-1])

    # 뒤 추가
    if sushi[s+k-1] not in su:
        su[sushi[s+k-1]] = 1
    else:
        su[sushi[s+k-1]] += 1
    cmp_sulen = len(su)

    # 보너스 체크
    if c not in su:
        cmp_sulen += 1

    longest = max(longest, cmp_sulen)
    #print(su, longest)
        
print(longest)