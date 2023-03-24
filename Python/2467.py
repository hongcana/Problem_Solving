import sys
read = sys.stdin.readline
N = int(read().rstrip())
li = list(map(int, read().split()))
start = 0
end = N-1
opt = 0
pos = [0, 0]
# 연산 시간 = O(N)
while start < end:
    # 종료 조건?
    # 최적의 값을 저장해야하는 변수
    tmp = li[start] + li[end]
    if tmp < 0:
        if start == 0:  # 처음이라면
            opt = abs(tmp)
            pos = [start, end]
        else:
            opt = min(abs(tmp), opt)
            if opt == abs(tmp):
                pos = [start, end]
        start += 1

    elif tmp > 0:
        if start == 0:  # 처음이라면
            opt = abs(tmp)
            pos = [start, end]
        else:
            opt = min(abs(tmp), opt)
            if opt == abs(tmp):
                pos = [start, end]
        end -= 1
    else:
        pos = [start, end]
        break
print(li[pos[0]], li[pos[1]])
