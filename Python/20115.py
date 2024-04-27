import sys
N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split(" ")))
li.sort()
sum = li[-1]

for i in range(N-1): 
    sum += li[i] / 2 

print(sum)

# 가장 큰거 가장 작은거
# 2 3 6 9 10
# 3 6 9 11
# 6 9 12.5
# 9 15.5
# 20