
# 서류 심사 결과로 정렬 (내림차순)
# 서류 심사 1등의 면접 순위를 살펴보고, 그 순위보다 낮은 사람 떨구기

# 기준점을 새롭게 붙은 사람으로 설정하기
# 그 사람보다 순위가 낮으면 떨구고, 그 사람도 통과면 새롭게 기준 설정 반복


count = int(input())

for c in range(0, count):
    num = int(input())

    applys = []
    for n in range(0, num):
        applys.append(list(map(int, input().split())))

    applys.sort(key=lambda x: x[0])  # 서류 심사 결과로 정렬(내림차순)
    stand = applys[0][1]

    cnt = 0
    for a in applys:
        if a[1] == stand:
            cnt += 1
        elif a[1] < stand:
            stand = a[1]
            cnt += 1
    print(cnt)


# 새롭게 배우거나 다시 익혀할 내용들:
# 2차원 정렬 | list.sort(key lambda x:x[0])
# list comprehension (selectable)
