import sys
read = sys.stdin.readline
N, M = map(int, read().split())
hole = list(map(int, read().split()))

start = 0
end = 0
# 부분합
tmp_sum = 0

# 기존 최고 합
result = 0

for start in range(N):

    # tmp_sum에 end를 N전까지 쭉 늘려보자.
    while tmp_sum < M and end < N:
        tmp_sum += hole[end]
        if tmp_sum > M:
            tmp_sum -= hole[end]
            break
        else:
            end += 1

    # while이 끝나는 조건은 end를 다 돌거나, 부분합이 M을 넘은것임
    if result < tmp_sum and tmp_sum <= M:
        result = tmp_sum

    tmp_sum -= hole[start]
    # 투포인터의 합이 M보다 작고, 기존 부분합보다 크면
print(result)
