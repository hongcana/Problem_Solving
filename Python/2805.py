import sys
read = sys.stdin.readline

N, M = map(int, read().split())
tree = list(map(int, read().split()))
max_val = max(tree)


def bs(tree, target, start, end):
    total = 0
    while start <= end:
        result = 0
        mid = (start + end) // 2  # 4
        for t in tree:
            if mid < t:
                result += t - mid

        # 나무를 더 잘라야 하는 경우
        if result < target:
            end = mid-1

        # 나무를 덜 잘라도 되는 경우
        else:
            total = mid
            start = mid+1
    return total


print(bs(tree, M, 0, max_val))
