
# 첨에는 홀수일때는 먹이를 주고
# 남은 체력이 짝수일때는 먹이를 주지 않는다고 생각

T = int(input())
ans = []
for _ in range(T):
    n, m = map(int, input().split(" "))
    day = 0
    while n != 0:
        n = n // 2
        day += 1    
    day += m
    ans.append(day)

for i in ans:
    print(i)

# 그냥 m만큼 횟수가 한 번 늘어나는 느낌인데.
# 2^t 에서 (t+1)만큼 생존하는가?
# (t+1)만큼 생존에 m만큼 쁠러스.
# 그냥 무작정 나누고 나중에 몰빵해주면 됨