import sys
read = sys.stdin.readline

N, K = map(int, read().split())
values = list(map(int, read().split()))
deq = []  # 각 차이를 계산하는 list

# 6 3
# 1 99 100 111 120 1000
# 인접한 키 차이는... 98 1 11 9 880
# 이거를 내림차순 하면.. 880 98 11 9 1

# 모든 조 별로 인원이 같을 필요는 없구나
# 그러면 [99, 100, 111, 120], [1000],[1]
# 와 능지 이슈

for i in range(0, len(values)-1):
    deq.append(values[i+1] - values[i])

deq.sort(reverse=True)
print(sum(deq[K-1:]))
