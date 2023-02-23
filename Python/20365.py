input()
li = input()

start = li[0]
result = []
count = 0
flag = -1

for i in li[flag::-1]:  # or use reversed(li)
    if i == start:
        for i in li[flag::-1]:
            result.append(start)
        count += 1
        break
    else:
        flag += -1

if start == 'B':
    i = 0
    while i < len(result):
        if li[i] == 'R':
            result[i] = 'R'
            j = i+1
            while j < len(result) and li[j] != 'B':
                result[j] = 'R'
                j += 1
            i = j
            count += 1
        else:
            i += 1

if start == 'R':
    i = 0
    while i < len(result):
        if li[i] == 'B':
            result[i] = 'B'
            j = i+1
            while j < len(result) and li[j] != 'R':
                result[j] = 'B'
                j += 1
            i = j
            count += 1
        else:
            i += 1


# result 나머지 li의 빨간색으로 연속 채우기
if len(result) != len(li):
    for i in range(len(result), len(li)):
        result.append('R')
    count += 1

print(count)
