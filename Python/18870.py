import sys
read = sys.stdin.readline
dic = {}
N = read().rstrip()
cp = list(map(int, read().split()))
li = sorted(list(set(cp)))
for i in range(len(li)):
    dic[li[i]] = i
for i in cp:
    print(dic[i], end=" ")