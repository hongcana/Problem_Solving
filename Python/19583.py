import sys

S, E, Q = map(str, sys.stdin.readline().split())
dic = {}
cnt = 0

# 시작 인원 등록
while True:
    try:
        time, nickname = map(str, sys.stdin.readline().split())

        if time <= S:
            dic[nickname] = True

        elif time >= E and time <= Q:
            if nickname not in dic:
                continue # 목록에 없으므로 계속 진행
            else:
                if dic[nickname]:
                    dic[nickname] = False
                    cnt += 1
    except:
        break

print(cnt)