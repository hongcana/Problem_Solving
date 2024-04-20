
# solve this problem using two pointer

import sys
X, N = map(int, sys.stdin.readline().split(" "))
blog = list(map(int, sys.stdin.readline().split(" ")))

# end = N-1

max_count = 0
max_value = 0

sum_blog = [ 0 for _ in range(len(blog))]

# 합을 일일이 구하지 말고
# 이전 합에서 - 윈도우 이전의 값 + 윈도우 이후의 값
# 이게 비용이 덜 들듯

for start in range(X-N+1):
    
    # 처음에는 일단 더함
    if start == 0:
        li_sum = sum(blog[start:start+N])
    
    else:
        li_sum = li_sum - blog[start-1] + blog[start+N-1]

    if li_sum > max_value:
        max_value = li_sum
        max_count = 1
    
    elif li_sum == max_value:
        max_count += 1


if max_value == 0:
    print("SAD")
else:
    print(max_value)
    print(max_count)