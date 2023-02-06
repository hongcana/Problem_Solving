cities = int(input())

dists = list(map(int, input().split()))
costs = list(map(int, input().split()))

total = costs[0] * dists[0]
min_costs = costs[0]

# 다음꺼보다 싸냐? => 지금에서 더 넣어
# 쭉 흝다가 어 다음께 더 싼대? 거기까지 넣어

for i in range(1, len(dists)):
    if min_costs <= costs[i]:
        total += min_costs * dists[i]
    else:
        total += costs[i] * dists[i]
        min_costs = costs[i]

print(total)