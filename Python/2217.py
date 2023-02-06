num = int(input())
ropes = []

for i in range(0, num):
    ropes.append(int(input()))
ropes.sort()

# 2 5 10 15
# 8? 가능(4개로) => 가장 중량이 낮은 로프
# 15 가능(3개로) => 해당 중량을 제외한 로프
# 20 가능(2개로) => 낮은거 또 짜른거
# 15 가능(1개로) => 제일 위에꺼

max_val = min(ropes) * len(ropes)
for i in range(1, len(ropes)):
    if max_val <= min(ropes) * len(ropes):
        max_val = min(ropes) * len(ropes)
    ropes.pop(0)

print(max_val)