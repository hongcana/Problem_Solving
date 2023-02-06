input()
tired = list(map(int, input().split()))
tired.sort(reverse=True)
maxi = tired[0]
if len(tired) % 2 != 0:
    tired.pop(0)

for i in range(0, len(tired) // 2):
    if maxi < max(tired) + min(tired):
        maxi = max(tired) + min(tired)
    tired.pop(0)
    tired.pop(-1)

print(maxi)

# 역순으로 정렬
# 홀수일 경우 -> 하나 빼서 최대 M값에 등록
# 짝수일 경우 -> max랑 min 합 비교

# max, min => O(n), but list indexing => O(1)