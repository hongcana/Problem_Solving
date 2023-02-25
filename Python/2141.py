# 전체 인구수의 절반이 넘는 거리에 세운다. ( 정말 탐욕적이네.. )
# 스스로 풀지 못했음. 힌트 봤음.

import sys
read = sys.stdin.readline

N = int(read())
towns = []
for i in range(N):
    towns.append(list(map(int, read().split())))

towns.sort(key=lambda x: x[0])

sum = 0
for t in towns:
    sum += t[1]

sum = round(sum/2)

cmp = 0
for j in range(0, len(towns)):
    cmp += towns[j][1]
    if cmp >= sum:
        print(towns[j][0])
        break
