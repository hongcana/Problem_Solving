import sys
read = sys.stdin.readline

N = int(read())
word = [list(map(lambda x: ord(x)-65, read().rstrip())) for _ in range(N)]
alphabets_list = [0] * 26

for i in range(N):
    j = 0
    for w in word[i][::-1]:
        alphabets_list[w] += (10 ** j)
        j += 1

# GCF
# ACDEB

# 알파벳 A = 10000
# 알파벳 B = 1
# 알파벳 C = 1010
# 알파벳 G = 100
# 알파벳 D = 100

alphabets_list.sort(reverse=True)
total = 0
mult = 9
for num in range(0, len(alphabets_list)):
    if alphabets_list[num] == 0:
        break
    else:
        total += alphabets_list[num] * mult
        mult -= 1

print(total)
