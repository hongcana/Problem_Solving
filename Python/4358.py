import heapq as hq
import sys
tree = []
dic = {}

while True:
    try:
        tr = sys.stdin.readline().rstrip()
        if tr == "":
            break
        else:

            hq.heappush(tree, tr)
    except:
        break

denom = len(tree)
while tree:
    key = hq.heappop(tree)
    if key not in dic:
        dic[key] = 0
    dic[key] += 1

for k, v in sorted(dic.items()):
    dic[k] = round((v/denom) * 100,4)
    print(f'{k} {dic[k]:.4f}')