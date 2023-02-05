# replace의 대단함
# replace 안풀고도 경우의 수 놀이하면 풀이 가능

li = input()

li = li.replace('XXXX', 'AAAA')
li = li.replace('XX', 'BB')

if 'X' in li:
    print(-1)

else:
    print(li)
