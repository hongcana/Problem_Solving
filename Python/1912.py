import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = list(map(int, read().split()))
dp = [0 for _ in range(len(li))]
dp[N-1] = li[N-1]

for i in range(N-2, -1, -1):
    dp[i] = max(li[i], dp[i+1]+li[i])

print(max(dp))

# 뒤에서 부터 돌아도 틀린건 아니고,

# 점화식을
# for i in range(1, N):
#   dp[i] = max(li[i], dp[i-1]+li[i])으로 세워서
# i-1번째 연속합과 자기 자신을 더한 값 vs 나부터 시작을 비교할 수 있음
# ex) 3 4 -4 6 5 = 14