num = int(input())
confs = []

for i in range(0, num):
    confs.append(list(map(int, input().split())))
confs.sort(key=lambda x: (x[1],x[0]))
count = 1

end_time = confs[0][1]

for i in range(1, num):
    if confs[i][0] >= end_time:
        count += 1
        end_time = confs[i][1]
print(count)