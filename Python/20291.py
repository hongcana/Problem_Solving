
dic = {}
N = int(input())

for _ in range(N):
    name, domain = map(str, input().split("."))

    if domain not in dic:
        dic[domain] = 1
    
    else:
        dic[domain] += 1

for k in sorted(dic.keys()):
    print(k, dic[k])