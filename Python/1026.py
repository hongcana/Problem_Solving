import sys
read = sys.stdin.readline
N = int(read())
one = list(map(int, read().split()))
two = list(map(int, read().split()))
one.sort()
two.sort(reverse=True)
sum = 0
for i in range(N):
    sum += one[i] * two[i]
print(sum)
